def chatbot():
    print("Chatbot: Hi! I am a simple chatbot.")
    print("Chatbot: You can say 'Hello', 'How are you', or 'Bye'.")

    while True:
        user_input = input("You: ").capitalize()

        if user_input == "Hello":
            print("Chatbot: Hi!")

        elif user_input == "How are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "Bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()


