import json
import re
import time
from pathlib import Path

import pdfplumber
from dotenv import load_dotenv
from openai import APIConnectionError, APITimeoutError, InternalServerError, OpenAI, RateLimitError

# -------------------------
# Paths
# -------------------------
INPUT_DIR = Path("input_pdfs")
OUTPUT_DIR = Path("output")
CONTRACT_PATH = Path("contract.md")

# -------------------------
# Settings
# -------------------------
MODEL_CONVERT = "gpt-4.1-mini"
MODEL_FLAG = "gpt-4.1-mini"
MAX_INPUT_CHARS = 120_000  # safety limit to avoid huge uploads by accident
MAX_RETRIES = 5
RETRY_BASE_DELAY = 2  # seconds; doubled each attempt

# Always append this (deterministic), regardless of what the model outputs
REVIEW_CHECKLIST_MD = """
## Review Checklist
- [ ] Growth conditions verified (temperature, CO2/O2, time)
- [ ] Media composition and volumes verified
- [ ] Mixing parameters verified (rpm/RCF, time)
- [ ] Incubation times verified
- [ ] Centrifugation settings verified (RCF, time, temp)
- [ ] Step order confirmed against source
- [ ] Any ambiguous values flagged with [CHECK]
""".strip()

# Explicitly load .env (important on Windows)
load_dotenv(dotenv_path=".env")


# -------------------------
# PDF extraction
# -------------------------
def extract_text_from_pdf(pdf_path: Path) -> str:
    parts: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            parts.append(f"\n\n--- PAGE {i} ---\n\n{text}")
    return "".join(parts).strip()


# -------------------------
# Cleaning helpers
# -------------------------
def remove_hyphen_linebreaks(text: str) -> str:
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def normalize_newlines(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n\s*\n+", "\n<BLANKLINE>\n", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    return text.replace("\n<BLANKLINE>\n", "\n\n")


def tidy_spaces(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = "\n".join(line.strip() for line in text.splitlines())
    return text.strip()


def clean_text(raw: str) -> str:
    cleaned = raw
    cleaned = remove_hyphen_linebreaks(cleaned)
    cleaned = normalize_newlines(cleaned)
    cleaned = tidy_spaces(cleaned)
    return cleaned

# -------------------------
# User-facing label normalization
# -------------------------
def normalize_user_facing_labels(md: str) -> str:
    """
    Normalize user-facing section titles to avoid AI-internal language.
    """
    replacements = {
        "Possible Hallucinations/Unsupported Claims": "Possible Unsupported Claims",
        "Possible Hallucinations / Unsupported Claims": "Possible Unsupported Claims",
        "Possible Hallucinations and Unsupported Claims": "Possible Unsupported Claims",
        "Possible Hallucinations": "Possible Unsupported Claims",
    }
    for old, new in replacements.items():
        md = md.replace(old, new)
    return md

# -------------------------
# Retry helper
# -------------------------
_RETRYABLE = (RateLimitError, APITimeoutError, APIConnectionError, InternalServerError)


def _call_with_retry(client: OpenAI, model: str, prompt: str) -> str:
    """Call the OpenAI responses API with exponential backoff on transient errors."""
    delay = RETRY_BASE_DELAY
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.responses.create(model=model, input=prompt)
            return resp.output_text.strip()
        except _RETRYABLE as e:
            if attempt == MAX_RETRIES:
                raise
            print(f"  ⏳ Retry {attempt}/{MAX_RETRIES} after {type(e).__name__}, waiting {delay}s …")
            time.sleep(delay)
            delay *= 2


# -------------------------
# LLM: conversion
# -------------------------
def convert_to_protocol_markdown(client: OpenAI, contract: str, cleaned_text: str) -> str:
    if len(cleaned_text) > MAX_INPUT_CHARS:
        cleaned_text = cleaned_text[:MAX_INPUT_CHARS] + "\n\n[TRUNCATED: input exceeded MAX_INPUT_CHARS]\n"

    prompt = f"""
You are a careful scientific editor.

Follow the protocol output contract STRICTLY.
Do not add or invent scientific content.
Preserve all numbers/units/times/temperatures exactly.
If something is unclear, write "[CHECK]" rather than guessing.

--- CONTRACT ---
{contract}

--- INPUT TEXT ---
{cleaned_text}
""".strip()

    return _call_with_retry(client, MODEL_CONVERT, prompt)


def finalize_protocol_md(protocol_md: str) -> str:
    if "## Review Checklist" in protocol_md:
        return protocol_md.strip() + "\n"
    return protocol_md.strip() + "\n\n" + REVIEW_CHECKLIST_MD + "\n"


# -------------------------
# LLM: flagging (second pass)
# -------------------------
def generate_flags_md(client: OpenAI, cleaned_text: str, protocol_md: str) -> str:
    # Keep the inputs bounded
    if len(cleaned_text) > 60_000:
        cleaned_text = cleaned_text[:60_000] + "\n\n[TRUNCATED]\n"
    if len(protocol_md) > 60_000:
        protocol_md = protocol_md[:60_000] + "\n\n[TRUNCATED]\n"

    prompt = f"""
You are a scientific QA reviewer. Your job is to flag risk, not to rewrite.

Given:
1) SOURCE TEXT (from a PDF extraction)
2) GENERATED PROTOCOL (Markdown)

Return a Markdown report with these sections:

## Critical Parameters Checklist (from the protocol)
List the key numeric parameters present in the generated protocol (e.g., temperatures, times, volumes, concentrations, rpm/RCF, CO2/O2).
If a category is not present, say "MISSING".

## Potential Missing Parameters (compare to source)
Identify parameters that appear in the SOURCE TEXT but are missing or unclear in the GENERATED PROTOCOL.
Only cite items that are supported by the SOURCE TEXT.

## Possible Unsupported Claims
List any statements in the GENERATED PROTOCOL that are NOT clearly supported by the SOURCE TEXT.
If none, say "None detected".

## Step Order / Omission Risks
Call out any suspected omitted steps or ordering changes.
If none, say "None detected".

Rules:
- Be conservative.
- If unsure, label as "[CHECK]" instead of asserting.
- Use short bullet points.

--- SOURCE TEXT ---
{cleaned_text}

--- GENERATED PROTOCOL ---
{protocol_md}
""".strip()

    return _call_with_retry(client, MODEL_FLAG, prompt)


def append_flags_summary(protocol_md: str, flags_md: str) -> str:
    """
    Add a short flags section at the end of protocol.md so users see it immediately.
    Keep it concise by extracting just the Potential Missing + Hallucinations headers if present.
    """
    # Normalize both inputs first
    protocol_md_norm = normalize_user_facing_labels(protocol_md)
    flags_md_norm = normalize_user_facing_labels(flags_md)

    if "## Review Flags" in protocol_md_norm:
        return protocol_md_norm

    result_md = protocol_md_norm.strip() + "\n\n## Review Flags\n\n" + flags_md_norm.strip() + "\n"
    # Ensure normalization to the final concatenated string as well
    result_md = normalize_user_facing_labels(result_md)
    return result_md


# -------------------------
# Main
# -------------------------
def main() -> None:
    if not CONTRACT_PATH.exists():
        raise SystemExit("Missing contract.md in project root. Create it first.")

    if not INPUT_DIR.is_dir():
        raise SystemExit(f"Input directory '{INPUT_DIR}' does not exist. Create it and add PDFs.")

    pdfs = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit("No PDFs found in input_pdfs/. Add PDFs and try again.")

    contract = CONTRACT_PATH.read_text(encoding="utf-8")
    client = OpenAI()

    # Validate API key early to avoid wasting time on PDF extraction
    try:
        client.models.list()
    except Exception as e:
        raise SystemExit(f"OpenAI API key check failed: {e}") from e

    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"Found {len(pdfs)} PDFs. Batch: convert={MODEL_CONVERT}, flag={MODEL_FLAG}")

    for pdf_path in pdfs:
        t0 = time.time()
        stem = pdf_path.stem
        out_dir = OUTPUT_DIR / stem
        out_dir.mkdir(parents=True, exist_ok=True)

        log = {
            "pdf": pdf_path.name,
            "started_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "model_convert": MODEL_CONVERT,
            "model_flag": MODEL_FLAG,
            "status": "started",
        }

        try:
            raw = extract_text_from_pdf(pdf_path)
            (out_dir / "raw_extracted.txt").write_text(raw, encoding="utf-8")

            cleaned = clean_text(raw)
            (out_dir / "cleaned.txt").write_text(cleaned, encoding="utf-8")

            if len(cleaned) < 500:
                log["warning"] = "Very low extracted text. PDF may be scanned/image-only."

            protocol_md = convert_to_protocol_markdown(client, contract, cleaned)
            protocol_md = finalize_protocol_md(protocol_md)

            # Flagging pass (QA)
            flags_md = generate_flags_md(client, cleaned, protocol_md)
            (out_dir / "flags.md").write_text(flags_md, encoding="utf-8")

            # Append flags into protocol for visibility
            protocol_with_flags = append_flags_summary(protocol_md, flags_md)
            (out_dir / "protocol.md").write_text(protocol_with_flags, encoding="utf-8")

            log["status"] = "success"
            log["raw_chars"] = len(raw)
            log["cleaned_chars"] = len(cleaned)
            log["elapsed_seconds"] = round(time.time() - t0, 2)

            print(f"✅ {pdf_path.name} -> {out_dir / 'protocol.md'}  ({log['elapsed_seconds']}s)")

        except Exception as e:
            log["status"] = "error"
            log["error"] = repr(e)
            log["elapsed_seconds"] = round(time.time() - t0, 2)
            print(f"❌ {pdf_path.name} failed: {e!r}")

        try:
            (out_dir / "run_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
        except OSError as e:
            print(f"⚠️  Could not write run_log.json for {pdf_path.name}: {e!r}")

    print("\nDone. Review outputs in output/<pdfname>/{protocol.md, flags.md}")


if __name__ == "__main__":
    main()
