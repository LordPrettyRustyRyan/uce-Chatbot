# Uce - a Chatbot

Uce is a fun, terminal-based AI assistant with a laid-back vibe, inspired by WWE's Bloodline (Jey & Jimmy Uso, Roman Reigns).
It’s **chill, comedic, and confident** — It delivers short, casual responses with slang like "Ayo" and "Yeet."

Built to work in both CLI (terminal) and Web (Flask + HTML/CSS/JS) without changing the chatbot logic.

## Features:
- Fun, casual “uce” energy (Jey & Jimmy Uso / Roman Reigns slang)
- Context-aware conversations — remembers chat history
- Quick, short, on-point answers — no fluff
- Handles casual exits like “seeya”, “ight later bruv”, etc.
- Easy to extend for more functionality

---

## Tech Stack & Libraries:
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2E6F9F?style=for-the-badge&logo=python&logoColor=white)
![Python Dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=for-the-badge&logo=python&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Chat Completions API](https://img.shields.io/badge/Chat_Completions_API-412991?style=for-the-badge&logo=openai&logoColor=white)

---

## Future Improvements
- Chat history persistence
- User sessions
- Dark / light theme toggle

---

## Website Preview
<img width="1920" height="1080" alt="Screenshot (2016)" src="https://github.com/user-attachments/assets/0f5f533f-b7c4-4197-b87e-f4c51a03465c" />

---

## How To Run:
1. Clone the repo:
    ```
    git clone https://github.com/Sidharath/Uce-Chatbot.git
    cd Uce-Chatbot
2. Install dependencies:
    ```
    pip install -r requirements.txt
3. Add your OpenAI API key to a .env file (in same folder where you keep _'uce.py'_:
    ```
    OPENAI_API_KEY = your_openai_key_here
4. Run CLI Version (Terminal):
    ```
    python cli.py
5. Run Web Version (Flask UI):
    ```
    python app.py
It runs on http://127.0.0.1:5000
Chat away!
