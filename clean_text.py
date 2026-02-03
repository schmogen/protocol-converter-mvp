import re
from pathlib import Path

INPUT_PATH = Path("output/raw_extracted.txt")
OUTPUT_PATH = Path("output/cleaned.txt")

def remove_hyphen_linebreaks(text: str) -> str:
    # Fix words split across lines: "centrifu-\nge" -> "centrifuge"
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)

def normalize_newlines(text: str) -> str:
    # Convert Windows newlines to Unix newlines for consistent processing
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Preserve blank lines as paragraph breaks:
    # - Temporarily mark blank lines
    text = re.sub(r"\n\s*\n+", "\n<BLANKLINE>\n", text)

    # Replace remaining single newlines with spaces (unwrap paragraphs)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

    # Restore blank lines
    text = text.replace("\n<BLANKLINE>\n", "\n\n")
    return text

def tidy_spaces(text: str) -> str:
    # Collapse repeated spaces
    text = re.sub(r"[ \t]+", " ", text)
    # Trim spaces on each line
    text = "\n".join(line.strip() for line in text.splitlines())
    return text.strip()

def main():
    if not INPUT_PATH.exists():
        raise SystemExit(f"Missing {INPUT_PATH}. Run extract_text.py first.")

    raw = INPUT_PATH.read_text(encoding="utf-8", errors="replace")

    cleaned = raw
    cleaned = remove_hyphen_linebreaks(cleaned)
    cleaned = normalize_newlines(cleaned)
    cleaned = tidy_spaces(cleaned)

    OUTPUT_PATH.write_text(cleaned, encoding="utf-8")
    print(f"✅ Cleaned text saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()