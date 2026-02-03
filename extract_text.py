from pathlib import Path
import pdfplumber

INPUT_DIR = Path("input_pdfs")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def extract_text(pdf_path: Path) -> str:
    parts = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            parts.append(f"\n\n--- PAGE {i} ---\n\n{text}")
    return "".join(parts).strip()

def main():
    pdfs = list(INPUT_DIR.glob("*.pdf"))
    if not pdfs:
        raise SystemExit("No PDFs found in input_pdfs/")

    pdf = pdfs[0]
    text = extract_text(pdf)

    out_path = OUTPUT_DIR / "raw_extracted.txt"
    out_path.write_text(text, encoding="utf-8")

    print(f"Extracted text from {pdf.name}")
    print(f"Saved to {out_path}")

if __name__ == "__main__":
    main()