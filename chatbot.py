def get_response(message):
    message = message.lower().strip()

    if any(word in message for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to Customer Support."

    elif "price" in message or "cost" in message:
        return "Please check our product page for prices."

    elif "order" in message:
        return "Please provide your order ID to track your order."

    elif "return" in message or "refund" in message:
        return "You can request a return or refund through customer support."

    elif "delivery" in message or "shipping" in message:
        return "Delivery usually takes 3 to 5 business days."

    elif "payment" in message:
        return "We support online payment methods."

    elif "thank" in message:
        return "You're welcome! Happy to help."

    elif "bye" in message:
        return "Thank you for contacting us. Goodbye!"

    else:
        return "Sorry, I didn't understand. Please ask about orders, prices, delivery, returns, or payments."


print("===================================")
print("     CUSTOMER SERVICE CHATBOT")
print("===================================")
print("Type 'bye' to exit.")

while True:
    user_message = input("\nYou: ")
    response = get_response(user_message)
    print("Bot:", response)

    if "bye" in user_message.lower().split():
        break