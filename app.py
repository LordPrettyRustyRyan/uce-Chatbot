from flask import Flask, render_template, request, jsonify
from uce import chat_with_AI

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")
    chat_history = data.get("chat_history", [])

    reply = chat_with_AI(user_message, chat_history)

    updated_history = chat_history + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": reply}
    ]

    return jsonify({
        "reply": reply,
        "chat_history": updated_history
    })

if __name__ == "__main__":
    app.run(debug=True)
