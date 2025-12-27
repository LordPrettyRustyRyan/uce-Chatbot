import os
import requests
from dotenv import load_dotenv

# ------------- Load API Key

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_KEY:
    raise RuntimeError("OPENAI_API_KEY not found in .env")

# ------------- Chat with OpenAI

def chat_with_AI(user_input, chat_history):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = {
        "role": "system",
        "content": "You are a friendly, confident AI assistant with a laid-back, hype 'uce' energy inspired by WWE Bloodline vibes. \
            You speak casually, use Jey Uso, Jimmy Uso, Roman Reigns slang phrases like 'Ayo', 'Yeet', 'waddup uce', 'we good', & 'know what i mean?' & more \
                and keep things chill and comedic. Keep responses short, on-point, and accurate. Sometimes address the user as 'OG'. \
                    Avoid over-wording. You keep responses fun and respectful, and explain things clearly while sounding like an awesome, \
                        trustworthy dude - cause we the ones, uce."
    }

    messages = [system_prompt] + chat_history + [
        {"role": "user", "content": user_input}
    ]

    payload = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 200
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)

    if response.status_code != 200:
        print("API Error:", response.text)
        return "Something went wrong."

    reply = response.json()["choices"][0]["message"]["content"]
    return reply.strip()

# -------------- MAIN LOOP

def main():
    print("=== Chatbot Initializing ===")
    print("Type 'exit' or 'quit' to stop.\n")

    chat_history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Uce: Goodbye Uce ☝️")
            break

        elif user_input.lower() in ["seeya", "see ya", "see you", "see ya bruv", "see ya uce", "later bruv", "ight later bruv", "ight later man"]:
            print("Uce: Alright, Catch ya later, man ☝️")
            break

        reply = chat_with_AI(user_input, chat_history)
        print(f"Uce: {reply}\n")

        # Save conversation history
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
