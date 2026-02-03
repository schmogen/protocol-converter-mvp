import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    load_dotenv(dotenv_path=".env")  # explicit, to avoid Windows path weirdness

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY missing. Put it in .env as OPENAI_API_KEY=sk-...")

    client = OpenAI(api_key=api_key)

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input="Reply with exactly: OK"
    )

    print(resp.output_text.strip())

if __name__ == "__main__":
    main()