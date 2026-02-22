"""update_expected_sections.py

One-time utility: reads each reference DOCX, extracts actual headings and
bold paragraph text, and updates the expected_sections field in the
corresponding ground truth JSON.
"""

import io
import json
import shutil
import tempfile
from pathlib import Path

from docx import Document

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
DOCX_DIR   = SCRIPT_DIR / "test_data" / "reference_docx"
GT_DIR     = SCRIPT_DIR / "test_data" / "ground_truth"


# ---------------------------------------------------------------------------
# DOCX helpers (same temp-copy approach as quality_scorer.py)
# ---------------------------------------------------------------------------

def load_docx(docx_path: Path) -> Document:
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
        shutil.copy2(docx_path, tmp.name)
        tmp_path = tmp.name
    try:
        with open(tmp_path, "rb") as f:
            return Document(io.BytesIO(f.read()))
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def extract_sections(doc: Document) -> list[str]:
    """Extract headings and fully-bold paragraphs as section headers.

    Rules applied after extraction:
    - Skip paragraphs longer than 120 characters
    - Skip paragraphs that are purely numeric
    - Deduplicate while preserving order
    """
    seen = set()
    results = []

    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            continue

        # Collect by heading style or fully-bold runs
        style_name = p.style.name if p.style else ""
        is_heading = "Heading" in style_name
        runs = [r for r in p.runs if r.text.strip()]
        is_bold = bool(runs) and all(r.bold for r in runs)

        if not (is_heading or is_bold):
            continue

        # Skip overly long text (bold body paragraphs, not headers)
        if len(text) > 120:
            continue

        # Skip purely numeric paragraphs
        if text.replace(".", "").replace(",", "").isdigit():
            continue

        # Deduplicate
        if text in seen:
            continue

        seen.add(text)
        results.append(text)

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    docx_files = sorted(DOCX_DIR.glob("*.docx"))
    if not docx_files:
        print(f"No DOCX files found in {DOCX_DIR}")
        return

    print(f"Updating expected_sections for {len(docx_files)} file(s)\n")
    print("=" * 70)

    for docx_path in docx_files:
        stem    = docx_path.stem
        gt_path = GT_DIR / f"{stem}.json"

        print(f"\n{stem}")
        print("-" * len(stem))

        if not gt_path.exists():
            print(f"  [SKIP] No ground truth JSON found at {gt_path.name}")
            continue

        # Load ground truth
        try:
            gt = json.loads(gt_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"  [ERROR] Could not read JSON: {exc}")
            continue

        old_sections = gt.get("expected_sections", [])

        # Load DOCX and extract sections
        try:
            doc          = load_docx(docx_path)
            new_sections = extract_sections(doc)
        except Exception as exc:
            print(f"  [ERROR] Could not process DOCX: {exc}")
            continue

        # Update and write
        gt["expected_sections"] = new_sections
        try:
            gt_path.write_text(
                json.dumps(gt, indent=2, ensure_ascii=False), encoding="utf-8"
            )
        except Exception as exc:
            print(f"  [ERROR] Could not write JSON: {exc}")
            continue

        print(f"  Sections: {len(old_sections)} -> {len(new_sections)}")
        if new_sections:
            for s in new_sections:
                print(f"    + {s}")
        else:
            print("  (no sections extracted)")

    print("\n" + "=" * 70)
    print("Done.")


if __name__ == "__main__":
    main()
