import re

print("Chatbot: Hi! I am your simple chatbot. Type 'bye' to exit.")

# Chatbot ka main loop
while True:
    user = input("You: ").lower()

    # Exit condition
    if user in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # Basic responses
    if re.search(r"hi|hello|hey", user):
        print("Chatbot: Hello! How can I help you today?")
    elif "your name" in user:
        print("Chatbot: I am a simple Python chatbot created for your internship.")
    elif "how are you" in user:
        print("Chatbot: I am doing great! Thanks for asking.")
    elif "help" in user:
        print("Chatbot: I can reply to greetings, tell my name, and say bye.")
    else:
        print("Chatbot: Sorry, I didn't understand that. Try saying 'hello' or 'help'.")