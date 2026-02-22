"""generate_ground_truth.py

Generate ground truth JSON files used by the quality scoring system.

Usage:
    python generate_ground_truth.py --pdf <filename_or_path>
    python generate_ground_truth.py --all
    python generate_ground_truth.py --all --overwrite
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import pdfplumber
from dotenv import load_dotenv
from openai import OpenAI

# ---------------------------------------------------------------------------
# Paths (all relative to this script's location)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
INPUT_DIR = (SCRIPT_DIR / "../../input_pdfs").resolve()
GROUND_TRUTH_DIR = SCRIPT_DIR / "test_data" / "ground_truth"
ENV_PATH = (SCRIPT_DIR / "../../.env").resolve()

REQUIRED_KEYS = {
    "pdf_name",
    "protocol_title",
    "version",
    "last_reviewed",
    "notes",
    "expected_sections",
    "critical_values",
    "key_reagents",
    "formatting_checks",
    "hallucination_watchlist",
}

SYSTEM_PROMPT = """\
You are a scientific protocol analyst. Given the full text of a laboratory \
protocol PDF, extract structured information and return it as a single valid \
JSON object with no preamble, no markdown fencing, and no explanation — just \
the raw JSON.

Return exactly this schema:
{
  "pdf_name": "<original filename including .pdf>",
  "protocol_title": "<full title of the protocol>",
  "version": "1.0",
  "last_reviewed": "<today's date as YYYY-MM-DD>",
  "notes": "<2-3 sentence summary of what this protocol does and what kind of document it is>",
  "expected_sections": ["<every section header present in the document, in order>"],
  "critical_values": [
    {
      "id": "cv_001",
      "description": "<what this value represents>",
      "value": "<numeric value as string, no units>",
      "unit": "<unit only>",
      "context_hint": "<single lowercase word likely to appear near this value in the text>"
    }
  ],
  "key_reagents": ["<every reagent, buffer, media, chemical, or kit component mentioned>"],
  "formatting_checks": {
    "has_numbered_steps": true,
    "headers_use_bold": true,
    "no_bare_tables": true,
    "inline_value_embedding": true
  },
  "hallucination_watchlist": ["<terms that should NEVER appear in this protocol's output — e.g. reagents or procedures from completely different protocol types, biosafety levels that don't apply, equipment not used in this workflow. Do NOT include terms that are expected to appear — only flag unexpected or impossible terms.>"]
}

Extract every critical numeric value you can find — temperatures, centrifuge \
speeds, volumes, times, concentrations, cell counts, pH values, percentages. \
Be exhaustive. Number the cv_ ids sequentially.\
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_pdf_text(pdf_path: Path) -> str:
    """Extract full text from a PDF using pdfplumber."""
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text(x_tolerance=3, y_tolerance=3)
            if text:
                pages.append(text)
    return "\n\n".join(pages)


def call_openai(client: OpenAI, pdf_name: str, pdf_text: str) -> str:
    """Send extracted PDF text to GPT-4o-mini and return the raw response."""
    user_message = (
        f"PDF filename: {pdf_name}\n\n"
        f"Today's date: {date.today().isoformat()}\n\n"
        f"Full extracted text:\n\n{pdf_text}"
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0,
    )
    return (response.choices[0].message.content or "").strip()


def validate_and_parse(raw: str) -> dict | None:
    """Parse JSON and check all required top-level keys are present.

    Returns the parsed dict on success, or None if parsing/validation fails.
    """
    # Strip markdown fencing if the model added it anyway
    text = raw.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        text = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        print(f"    [ERROR] JSON parse failed: {exc}")
        return None

    missing = REQUIRED_KEYS - set(data.keys())
    if missing:
        print(f"    [WARN] Missing required keys: {missing}")
        return None

    return data


def process_pdf(pdf_path: Path, client: OpenAI, overwrite: bool = False) -> bool:
    """Process a single PDF and write its ground truth JSON.

    Returns True on success, False on any failure.
    """
    stem = pdf_path.stem
    out_json = GROUND_TRUTH_DIR / f"{stem}.json"
    out_raw = GROUND_TRUTH_DIR / f"{stem}.raw"

    if out_json.exists() and not overwrite:
        print(f"[SKIP] {pdf_path.name}  (already exists — pass --overwrite to replace)")
        return True

    print(f"[...] {pdf_path.name}")

    # 1. Extract text
    try:
        text = extract_pdf_text(pdf_path)
    except Exception as exc:
        print(f"    [ERROR] pdfplumber extraction failed: {exc}")
        return False

    if len(text) < 200:
        print(f"    [WARN] Only {len(text)} characters extracted — PDF may be image-based. Skipping.")
        return False

    # 2. Call OpenAI
    try:
        raw = call_openai(client, pdf_path.name, text)
    except Exception as exc:
        print(f"    [ERROR] OpenAI call failed: {exc}")
        return False

    # 3. Validate JSON
    data = validate_and_parse(raw)
    if data is None:
        out_raw.write_text(raw, encoding="utf-8")
        print(f"    [WARN] Saved raw response to {out_raw.name} for inspection.")
        return False

    # 4. Write output
    out_json.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    n_cv = len(data.get("critical_values", []))
    n_sec = len(data.get("expected_sections", []))
    print(f"    [OK] {out_json.name}  —  {n_cv} critical values, {n_sec} sections")
    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate ground truth JSON files for the quality scoring system."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--pdf",
        metavar="PATH",
        help="Path or filename of a single PDF to process.",
    )
    group.add_argument(
        "--all",
        action="store_true",
        help="Process all PDFs in input_pdfs/.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-generate even if a ground truth file already exists (--all mode only).",
    )
    args = parser.parse_args()

    # Load environment and create client
    load_dotenv(dotenv_path=ENV_PATH)
    client = OpenAI()

    # Ensure output directory exists
    GROUND_TRUTH_DIR.mkdir(parents=True, exist_ok=True)

    if args.pdf:
        pdf_path = Path(args.pdf)
        if not pdf_path.is_absolute() and not pdf_path.exists():
            # Bare filename — look in the default input directory
            pdf_path = INPUT_DIR / pdf_path
        if not pdf_path.exists():
            sys.exit(f"[ERROR] PDF not found: {pdf_path}")
        success = process_pdf(pdf_path, client, overwrite=True)
        sys.exit(0 if success else 1)

    # --all mode
    pdfs = sorted(INPUT_DIR.glob("*.pdf"))
    if not pdfs:
        sys.exit(f"[ERROR] No PDFs found in {INPUT_DIR}")

    print(f"Found {len(pdfs)} PDFs in {INPUT_DIR}\n")
    succeeded, failed, skipped = [], [], []

    for pdf_path in pdfs:
        stem = pdf_path.stem
        out_json = GROUND_TRUTH_DIR / f"{stem}.json"
        if out_json.exists() and not args.overwrite:
            print(f"[SKIP] {pdf_path.name}  (already exists — pass --overwrite to replace)")
            skipped.append(pdf_path.name)
            continue
        ok = process_pdf(pdf_path, client, overwrite=args.overwrite)
        (succeeded if ok else failed).append(pdf_path.name)

    print(f"\n{'='*60}")
    print(f"Results: {len(succeeded)} succeeded, {len(failed)} failed, {len(skipped)} skipped")
    if succeeded:
        print("\nSucceeded:")
        for name in succeeded:
            print(f"  [OK] {name}")
    if failed:
        print("\nFailed:")
        for name in failed:
            print(f"  [FAIL] {name}")
    if skipped:
        print("\nSkipped (already exist):")
        for name in skipped:
            print(f"  - {name}")


if __name__ == "__main__":
    main()
