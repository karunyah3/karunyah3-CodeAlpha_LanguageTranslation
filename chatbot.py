from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# FAQ data
questions = [
    "hello",
    "what is ai",
    "what is python",
    "how are you",
    "bye"
]

answers = [
    "Hi! How can I help you?",
    "AI stands for Artificial Intelligence.",
    "Python is a programming language.",
    "I am just a bot, but I'm doing great!",
    "Goodbye! Have a nice day!"
]

# Vectorize questions
vectorizer = CountVectorizer().fit_transform(questions)

def get_response(user_input):
    user_vec = CountVectorizer().fit(questions + [user_input]).transform(questions + [user_input])
    similarity = cosine_similarity(user_vec[-1], user_vec[:-1])
    
    index = similarity.argmax()
    
    if similarity[0][index] > 0:
        return answers[index]
    else:
        return "Sorry, I don't understand."

# Chat loop
while True:
    user = input("You: ").lower()
    
    if user == "exit":
        print("Bot: Goodbye!")
        break
    
    response = get_response(user)
    print("Bot:", response)