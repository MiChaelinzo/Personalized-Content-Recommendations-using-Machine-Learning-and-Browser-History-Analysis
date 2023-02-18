from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define a list of sample texts
texts = ["This is a positive review", "This is a negative review"]

# Create a TfidfVectorizer to extract features from the text
vectorizer = TfidfVectorizer()

# Fit the vectorizer to the text data
X = vectorizer.fit_transform(texts)

# Define the labels for the text data
y = [1, 0]  # 1 for positive, 0 for negative

# Create a Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier on the text data
clf.fit(X, y)

# Predict the sentiment of a new piece of text
new_text = "This is a great product"
new_X = vectorizer.transform([new_text])
predicted_sentiment = clf.predict(new_X)
print(predicted_sentiment)  # 1 (positive)
