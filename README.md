# Uce - a Chatbot

![WhatsApp Image 2025-12-25 at 12 44 08 AM](https://github.com/user-attachments/assets/6a3be178-f76d-4a39-8245-277f18d966d7)

Uce is a fun, terminal-based AI assistant with a laid-back vibe, inspired by WWE's Bloodline (Jey & Jimmy Uso, Roman Reigns).
It’s **chill, short, comedic, and confident** — It delivers short, casual responses with slang like "Ayo" and "Yeet."

It keeps conversation context, so it actually **remembers what you said**.  

---

## Features:
- Terminal-based Python chatbot
- Fun, casual “uce” energy (Jey & Jimmy Uso / Roman Reigns slang)
- Context-aware conversations — remembers chat history
- Quick, short, on-point answers — no fluff
- Handles casual exits like “seeya”, “ight later bruv”, etc.
- Easy to extend for more functionality

---

## Libraries Used:
- `requests` — API requests  
- `dotenv` — load your OpenAI API key  

---

## How To Run:
1. Clone the repo:
    ```
    git clone https://github.com/Sidharath/Uce-Chatbot.git
    cd Uce-Chatbot
2. Install dependencies:
    ```
    pip install requests python-dotenv
3. Add your OpenAI API key to a .env file (in same folder where you keep _'ucebot.py'_:
    ```
    OPENAI_API_KEY = your_openai_key_here
4. Run the chatbot:
    ```
    python uce_chatbot.py
Chat away!
