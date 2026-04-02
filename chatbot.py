faq = {
    "hello": "Hi! How can I help you?",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "bye": "Goodbye! Have a nice day!"
}

while True:
    user = input("You: ").lower()
    
    if user in faq:
        print("Bot:", faq[user])
    else:
        print("Bot: Sorry, I don't understand.")