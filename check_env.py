import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY", "")

print("Key loaded:", bool(key))
print("Key starts with:", key[:7])
print("Key length:", len(key))