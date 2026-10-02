import os
import json
from dotenv import load_dotenv

import requests 


load_dotenv()

url = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("API_KEY")
db = "model/main_memory.json"

if os.path.exists(db):
    with open(db, "r", encoding="utf-8") as f:
        memory = json.load(f)
else:
    memory = [{"role":"system", "content": "your name is Tyzon my assitant built for my support and help me with my daily tasks, coding, project handling and more."}]

header = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:

    data = {
        "model": "openai/gpt-luna-latest",
        "messages": memory
    }

    command = input("Enter your command: ")

    memory.append({"role": "user", "content": command})

    response = requests.post(
        url,
        headers=header,
        json=data
    )

    response.raise_for_status()

    result = response.json()

    tyzon_reply = result["choices"][0]["message"]["content"]

    memory.append({"role": "assistant", "content": tyzon_reply})

    print(f"Tyzon: {tyzon_reply}")

    with open(db, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4) #over
