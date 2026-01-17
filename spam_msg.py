
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Load the dataset
data = pd.read_csv("spam_msg.csv")

# Convert labels to numbers
# spam = 1, not spam = 0
data['label'] = data['label'].map({'spam': 1, 'not spam': 0})

#  Separate features & target
X = data['message']
y = data['label']

#  Convert text to numbers
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

#  Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.25, random_state=42
)

# Train the ML model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)


#  Test custom messages
print("\n--- Spam Message Detector ---")
print("Type 'exit' to stop")

while True:
    user_message = input("\nEnter a message: ")
    
    if user_message.lower() == 'exit':
        print("Program ended.")
        break

    message_vector = vectorizer.transform([user_message])
    result = model.predict(message_vector)

    if result[0] == 1:
        print("Prediction: SPAM ❌")
    else:
        print("Prediction: NOT SPAM ✅")
