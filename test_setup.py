from ollama import chat
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv('MODEL')
if not model:
    print("Error: MODEL environment variable not set in .env file")
    exit(1)

try:
    response = chat(
        model=model,
        messages=[{'role': 'user', 'content': 'Hello!'}],
    )
    print(response.message.content)
except Exception as e:
    print(f"Error: {e}")
    print(f"Model '{model}' not found. Pull it with: ollama pull {model}")