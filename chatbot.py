def chatbot():
    print("🤖 Hello! I am ChatBot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Bot: Goodbye! Have a nice day 👋")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm functioning as expected! 😊")
        elif "name" in user_input:
            print("Bot: I’m a simple chatbot made in Python!")
        elif "help" in user_input:
            print("Bot: Sure, I can help! Ask me something simple like greetings or about myself.")
        elif "bye" in user_input:
            print("Bot: Bye! Type 'exit' to close the chat.")
        else:
            print("Bot: Sorry, I didn’t understand that. Can you try something else?")

if __name__ == "__main__":
    chatbot()