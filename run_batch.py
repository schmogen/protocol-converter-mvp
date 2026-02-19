import argparse
import json
import re
import time
from pathlib import Path

import pdfplumber
from docx import Document
from docx.shared import Pt
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
def _table_to_markdown(table_data: list) -> str:
    """Convert pdfplumber table data (list of rows) to markdown pipe format."""
    if not table_data:
        return ""
    rows = []
    for row in table_data:
        cells = [str(cell).strip().replace("\n", " ") if cell is not None else "" for cell in row]
        rows.append("| " + " | ".join(cells) + " |")
    if len(rows) >= 1:
        num_cols = len(table_data[0])
        separator = "| " + " | ".join(["---"] * num_cols) + " |"
        rows.insert(1, separator)
    return "\n".join(rows)


def _extract_page_content(page) -> str:
    """Extract text and tables from a page, interleaved by vertical position."""
    tables = page.find_tables()
    if not tables:
        return page.extract_text() or ""

    # Sort tables by their top y-coordinate
    tables_sorted = sorted(tables, key=lambda t: t.bbox[1])

    blocks: list[tuple[float, float, str]] = []  # (top_y, bottom_y, content)

    # Build table markdown blocks
    for table in tables_sorted:
        x0, top, x1, bottom = table.bbox
        data = table.extract()
        if data:
            blocks.append((top, bottom, _table_to_markdown(data)))

    # Build crop regions for text between/around tables
    crop_regions: list[tuple[float, float]] = []
    prev_bottom: float = 0.0
    for table in tables_sorted:
        top = table.bbox[1]
        bottom = table.bbox[3]
        if top > prev_bottom:
            crop_regions.append((prev_bottom, top))
        prev_bottom = bottom
    if prev_bottom < page.height:
        crop_regions.append((prev_bottom, page.height))

    for region_top, region_bottom in crop_regions:
        cropped = page.crop((0, region_top, page.width, region_bottom))
        text = cropped.extract_text() or ""
        if text.strip():
            blocks.append((region_top, region_bottom, text))

    # Sort all blocks by top_y and join
    blocks.sort(key=lambda b: b[0])
    return "\n\n".join(content for _, _, content in blocks)


def _extract_page_content_with_placeholders(page, counter_start: int) -> tuple:
    """Like _extract_page_content but replaces each table with a TABLE_PLACEHOLDER_N
    token.  Returns (page_content_str, number_of_tables_found)."""
    tables = page.find_tables()
    if not tables:
        return page.extract_text() or "", 0

    tables_sorted = sorted(tables, key=lambda t: t.bbox[1])
    blocks: list[tuple[float, float, str]] = []
    counter = counter_start

    for table in tables_sorted:
        x0, top, x1, bottom = table.bbox
        rows = table.extract()
        if rows:
            blocks.append((top, bottom, f"TABLE_PLACEHOLDER_{counter}"))
            counter += 1

    n_tables = counter - counter_start

    crop_regions: list[tuple[float, float]] = []
    prev_bottom: float = 0.0
    for table in tables_sorted:
        top = table.bbox[1]
        bottom = table.bbox[3]
        if top > prev_bottom:
            crop_regions.append((prev_bottom, top))
        prev_bottom = bottom
    if prev_bottom < page.height:
        crop_regions.append((prev_bottom, page.height))

    for region_top, region_bottom in crop_regions:
        cropped = page.crop((0, region_top, page.width, region_bottom))
        text = cropped.extract_text() or ""
        if text.strip():
            blocks.append((region_top, region_bottom, text))

    blocks.sort(key=lambda b: b[0])
    return "\n\n".join(content for _, _, content in blocks), n_tables


def extract_tables_from_pdf(pdf_path: Path) -> list:
    """Return all tables from the PDF in page/vertical order as raw row data.

    Each entry is a dict with:
      'page'  – 1-based page number
      'top'   – top y-coordinate of the table on its page (pdfplumber coords)
      'rows'  – list[list[str|None]] from pdfplumber table.extract()
    """
    tables: list[dict] = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            for table in sorted(page.find_tables(), key=lambda t: t.bbox[1]):
                rows = table.extract()
                if rows:
                    tables.append({
                        "page": page_num,
                        "top": table.bbox[1],
                        "rows": rows,
                    })
    return tables


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract page text with TABLE_PLACEHOLDER_N tokens where tables appear."""
    parts: list[str] = []
    table_counter = 1
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            content, n_tables = _extract_page_content_with_placeholders(page, table_counter)
            table_counter += n_tables
            parts.append(f"\n\n--- PAGE {i} ---\n\n{content}")
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


# Matches a TABLE_PLACEHOLDER_N token that occupies its own line.
_PLACEHOLDER_LINE_RE = re.compile(r"^(TABLE_PLACEHOLDER_\d+)$", re.MULTILINE)


def clean_text_preserving_placeholders(raw: str) -> str:
    """Like clean_text but keeps TABLE_PLACEHOLDER_N tokens on their own lines.

    clean_text's normalize_newlines step collapses single newlines to spaces,
    which would inline placeholder tokens with surrounding text.  This function
    splits the raw string on placeholder lines, applies clean_text to each
    non-placeholder segment independently, then reassembles with each placeholder
    on its own blank-line-separated paragraph.
    """
    # re.split with a capturing group interleaves text and placeholder segments.
    segments = _PLACEHOLDER_LINE_RE.split(raw)
    result_parts: list[str] = []
    for seg in segments:
        if _PLACEHOLDER_LINE_RE.match(seg.strip()):
            result_parts.append("\n\n" + seg.strip() + "\n\n")
        else:
            result_parts.append(clean_text(seg))
    return "".join(result_parts).strip()

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
            print(f"  Retry {attempt}/{MAX_RETRIES} after {type(e).__name__}, waiting {delay}s...")
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

STEP COMPLETENESS: Every numbered step must begin with a verb or subject and be a fully self-contained sentence. If the source text for a step begins mid-sentence, reconstruct the full sentence before outputting it. Never output a step that begins with a lowercase letter, a conjunction (such as and, or, but, so, then, while), or a word that implies a preceding clause.

SECTION HEADINGS: Output every section heading from the source document as its own standalone markdown heading using the exact wording from the source. This includes passage labels such as "Passage 1", "Passage 2", "Passage 3-5" and any other named or numbered subsections — each must appear as a separate heading and must not be merged with adjacent section titles or wrapped in parentheses as part of another heading. Do not reorder or rename any section. Do not add any section headings that do not exist in the source document, including headings such as "Objective", "Procedure", or "Materials" unless those exact words appear as headings in the source.

SOURCE FIDELITY: Do not add any sections, content, checklists, flags, or commentary that does not exist in the source document. The output must contain only what is present in the source. Do not add review checklists, parameter summaries, missing-parameter analysis, unsupported-claims sections, or any other AI-generated content.

REAGENT DEFINITIONS: When a protocol step references a named reagent mixture (e.g. "recommended growth medium", "complete medium", or any reagent given a proper name), include the full composition of that mixture either inline in that step as a sub-bullet or in a Materials section at the top of the document. Do not reference a named mixture without defining it somewhere in the document.

NUMBERED STEPS: Output every procedural step as a markdown numbered list item using the format "1. text", "2. text", and so on. Every procedural step in the source must appear as a numbered list item in the output. Do not let any step fall through to plain text.

LIST NUMBERING: Whenever a new section or subsection heading appears, any numbered list that follows must restart at 1. Each procedural section is independent and must have its own numbering starting from 1.

TABLES: Tables from the source document have been replaced with placeholder tokens of the form TABLE_PLACEHOLDER_N (where N is a sequential integer starting from 1). When you encounter a TABLE_PLACEHOLDER_N token in the input, output that exact token verbatim on its own line at the same position relative to surrounding steps and headings. Do not reproduce any table data, do not convert table content to text or bullets, and do not reorder, skip, or merge placeholder tokens.

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
# Markdown -> Word export
# -------------------------
_HEADING_MAP = {"# ": 1, "## ": 2, "### ": 3}


def _parse_markdown_table(table_lines: list) -> list:
    """Parse markdown table lines into a list of rows (each a list of cell strings).
    Separator rows (| --- | --- |) are skipped."""
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        # Skip separator row — cells contain only dashes, colons, spaces
        inner = line.strip("|")
        if re.match(r"^[\s\-|:]+$", inner):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        rows.append(cells)
    return rows


def _add_table_to_doc(doc, table_lines: list) -> None:
    """Create a python-docx Table from markdown table lines."""
    rows = _parse_markdown_table(table_lines)
    if not rows:
        return

    num_cols = max(len(row) for row in rows)
    tbl = doc.add_table(rows=len(rows), cols=num_cols)
    tbl.style = "Table Grid"

    for r_idx, row_data in enumerate(rows):
        row = tbl.rows[r_idx]
        for c_idx in range(num_cols):
            cell_text = row_data[c_idx] if c_idx < len(row_data) else ""
            cell = row.cells[c_idx]
            cell.text = cell_text
            if r_idx == 0:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.bold = True


def _split_table_blocks(table_lines: list) -> list:
    """Split a flat list of consecutive pipe-delimited lines into individual
    table blocks.  A separator row (cells containing only dashes/colons) that
    appears after the first two lines of the current block signals that the
    preceding line is the header of a new table.  That line is moved into a
    fresh block together with the separator, and the old block is closed.
    """
    if not table_lines:
        return []

    def _is_sep(line: str) -> bool:
        inner = line.strip().strip("|")
        return bool(inner and re.match(r"^[\s\-|:]+$", inner))

    blocks = []
    current = []
    for line in table_lines:
        if _is_sep(line) and len(current) >= 2:
            blocks.append(current[:-1])
            current = [current[-1], line]
        else:
            current.append(line)
    if current:
        blocks.append(current)
    return blocks


def md_to_docx(md_text: str, docx_path: Path, pdf_tables: list = None) -> None:
    """Convert a Markdown protocol string to a .docx file with basic formatting.

    pdf_tables – ordered list of raw table dicts from extract_tables_from_pdf().
    When present, TABLE_PLACEHOLDER_N lines are replaced with the corresponding
    pre-extracted table rendered directly from pdfplumber row data.
    """
    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip blank lines (Word handles paragraph spacing)
        if not stripped:
            i += 1
            continue

        # TABLE_PLACEHOLDER_N — substitute the pre-extracted PDF table
        m_ph = re.match(r"^TABLE_PLACEHOLDER_(\d+)$", stripped)
        if m_ph:
            idx = int(m_ph.group(1)) - 1  # convert 1-based N to 0-based index
            if pdf_tables and 0 <= idx < len(pdf_tables):
                md_lines = _table_to_markdown(pdf_tables[idx]["rows"]).splitlines()
                _add_table_to_doc(doc, md_lines)
            i += 1
            continue

        # Detect start of a markdown table
        if stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            for block in _split_table_blocks(table_lines):
                _add_table_to_doc(doc, block)
            continue

        # Headings
        heading_level = None
        for prefix, level in _HEADING_MAP.items():
            if stripped.startswith(prefix):
                heading_level = level
                stripped = stripped[len(prefix):]
                break
        if heading_level is not None:
            doc.add_heading(stripped, level=heading_level)
            i += 1
            continue

        # Checkbox list items: - [ ] or - [x]
        if re.match(r"^- \[[ x]\] ", stripped):
            doc.add_paragraph(stripped[2:], style="List Bullet")
            i += 1
            continue

        # Bullet list items
        if stripped.startswith("- "):
            doc.add_paragraph(stripped[2:], style="List Bullet")
            i += 1
            continue

        # Numbered list items (e.g. "1. Step text")
        m = re.match(r"^(\d+)\.\s+", stripped)
        if m:
            doc.add_paragraph(stripped[m.end():], style="List Number")
            i += 1
            continue

        # Regular paragraph
        doc.add_paragraph(stripped)
        i += 1

    doc.save(str(docx_path))


# -------------------------
# Main
# -------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Convert protocol PDFs to Markdown and Word.")
    parser.add_argument("--file", type=Path, help="Path to a single PDF to convert instead of the entire input folder.")
    args = parser.parse_args()

    if not CONTRACT_PATH.exists():
        raise SystemExit("Missing contract.md in project root. Create it first.")

    if args.file:
        if not args.file.exists():
            raise SystemExit(f"File not found: {args.file}")
        pdfs = [args.file]
    else:
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
            pdf_tables = extract_tables_from_pdf(pdf_path)

            raw = extract_text_from_pdf(pdf_path)
            (out_dir / "raw_extracted.txt").write_text(raw, encoding="utf-8")

            cleaned = clean_text_preserving_placeholders(raw)
            (out_dir / "cleaned.txt").write_text(cleaned, encoding="utf-8")
            (out_dir / "cleaned_debug.txt").write_text(cleaned, encoding="utf-8")

            if len(cleaned) < 500:
                log["warning"] = "Very low extracted text. PDF may be scanned/image-only."

            protocol_md = convert_to_protocol_markdown(client, contract, cleaned)
            (out_dir / "model_output_debug.txt").write_text(protocol_md, encoding="utf-8")
            protocol_md = finalize_protocol_md(protocol_md)

            # Flagging pass (QA)
            flags_md = generate_flags_md(client, cleaned, protocol_md)
            (out_dir / "flags.md").write_text(flags_md, encoding="utf-8")

            # Append flags into protocol for visibility
            protocol_with_flags = append_flags_summary(protocol_md, flags_md)
            (out_dir / "protocol.md").write_text(protocol_with_flags, encoding="utf-8")

            # Export to Word — pass pre-extracted tables for placeholder substitution
            md_to_docx(protocol_with_flags, out_dir / "protocol.docx", pdf_tables)

            log["status"] = "success"
            log["raw_chars"] = len(raw)
            log["cleaned_chars"] = len(cleaned)
            log["elapsed_seconds"] = round(time.time() - t0, 2)

            print(f"[OK] {pdf_path.name} -> {out_dir / 'protocol.md'}  ({log['elapsed_seconds']}s)")

        except Exception as e:
            log["status"] = "error"
            log["error"] = repr(e)
            log["elapsed_seconds"] = round(time.time() - t0, 2)
            print(f"[FAIL] {pdf_path.name} failed: {e!r}")

        try:
            (out_dir / "run_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
        except OSError as e:
            print(f"[WARN] Could not write run_log.json for {pdf_path.name}: {e!r}")

    print("\nDone. Review outputs in output/<pdfname>/{protocol.md, flags.md}")


if __name__ == "__main__":
    main()
