from uce import chat_with_AI

def main():
    print("=== Chatbot Initializing ===")
    print("Type 'exit' or 'quit' to stop.\n")

    chat_history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Uce: Goodbye Uce ☝️")
            break

        elif user_input.lower() in [
            "seeya", "see ya", "see you", "see ya bruv",
            "see ya uce", "later bruv", "ight later bruv",
            "ight later man"
        ]:
            print("Uce: Alright, Catch ya later, man ☝️")
            break

        reply = chat_with_AI(user_input, chat_history)
        print(f"Uce: {reply}\n")

        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
