from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

# Training data for intent classification
training_data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("how are you", "greeting"),
    ("goodbye", "farewell"),
    ("bye", "farewell"),
    ("what's up", "greeting"),
    ("help", "assistance"),
    ("can you assist me", "assistance")
]

# Split data into messages and labels
messages, labels = zip(*training_data)

# Initialize the vectorizer and model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)
model = MultinomialNB()
model.fit(X, labels)

# Define response options for each intent
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "assistance": ["Sure, how can I help?", "What do you need assistance with?"]
}

# Function to predict the intent and respond
def get_response(user_message):
    X_test = vectorizer.transform([user_message])
    intent = model.predict(X_test)[0]
    return random.choice(responses.get(intent, ["I'm not sure how to respond to that."]))
