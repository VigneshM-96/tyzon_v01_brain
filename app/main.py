import os
from dotenv import load_dotenv

import requests

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
url = "https://openrouter.ai/api/v1/chat/completions"

headers={
    "Authorization":f"Bearer {API_KEY}",
    "Content-Type":"application/json"
}

data={
    "model":"openai/gpt-chat-latest",
    "messages":[
        {
            "role":"user",
            "content":"Tell me about ASI in AI era"
        }
    ]
}

response = requests.post(
    url,
    headers=headers,
    json=data
)

result = response.json()

print(result["choices"][0]["message"]["content"])