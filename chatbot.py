
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training sentences
training_sentences = [
    "hello", "hi", "hey", "good morning",
    "what can you do", "help me", "your features",
    "thank you", "thanks",
    "goodbye", "bye", "see you"
]

# Corresponding intents
training_intents = [
    "greeting", "greeting", "greeting", "greeting",
    "help", "help", "help",
    "thanks", "thanks",
    "goodbye", "goodbye", "goodbye"
]

# Responses
responses = {
    "greeting": "Hello! How can I help you?",
    "help": "I can tell you the time and date, search Google, and check the weather.",
    "thanks": "You're welcome!",
    "goodbye": "Goodbye!"
}

# Train the NLP model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)

model = LogisticRegression()
model.fit(X, training_intents)


def get_chatbot_response(command):
    command_vector = vectorizer.transform([command])

    probabilities = model.predict_proba(command_vector)[0]
    best_index = probabilities.argmax()

    confidence = probabilities[best_index]
    intent = model.classes_[best_index]

    if confidence < 0.35:
        return "Sorry, I don't understand that yet."

    return responses.get(intent, "Sorry, I don't understand that yet.")


# Test chatbot separately
if __name__ == "__main__":
    while True:
        text = input("You: ")

        if text.lower() in ["exit", "stop"]:
            break

        print("Assistant:", get_chatbot_response(text))
