from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Explicitly load .env (important on Windows)
load_dotenv(dotenv_path=".env")

CLEANED_PATH = Path("output/cleaned.txt")
CONTRACT_PATH = Path("contract.md")
OUT_PATH = Path("output/protocol.md")

def main():
    if not CLEANED_PATH.exists():
        raise SystemExit("Missing output/cleaned.txt. Run clean_text.py first.")

    if not CONTRACT_PATH.exists():
        raise SystemExit("Missing contract.md.")

    cleaned_text = CLEANED_PATH.read_text(encoding="utf-8", errors="replace")
    contract = CONTRACT_PATH.read_text(encoding="utf-8")

    prompt = f"""
You are a careful scientific editor.

Follow the protocol output contract STRICTLY.
Do not add or invent information.

--- CONTRACT ---
{contract}

--- INPUT TEXT ---
{cleaned_text}
"""

    client = OpenAI()

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    output = resp.output_text.strip()
    OUT_PATH.write_text(output, encoding="utf-8")

    print("✅ Protocol created:", OUT_PATH)

if __name__ == "__main__":
    main()