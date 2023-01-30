def chatbot():
    print("Hi, I am a Rule-based Chatbot. How can I help you?")
    while True:
        user_input = input("You: ")
        if "hello" in user_input.lower() or "hi" in user_input.lower():
            print("Chatbot: Hello! How are you today?")
        elif "how are you" in user_input.lower():
            print("Chatbot: I'm good, thank you. How about you?")
        elif "goodbye" in user_input.lower() or "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand what you're saying. Could you please rephrase?")

chatbot()
