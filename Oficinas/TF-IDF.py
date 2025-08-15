from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=5000, stop_words="portuguese")
X = vectorizer.fit_transform(emails)