from glove import Corpus, Glove
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "The cat in the hat.",
    "The hat on the cat."
]

# Tokenize the documents
tokenized_documents = [word_tokenize(doc.lower()) for doc in documents]

# Create a CountVectorizer to get the vocabulary and co-occurrence matrix
vectorizer = CountVectorizer()
co_occurrence_matrix = vectorizer.fit_transform([" ".join(doc) for doc in tokenized_documents]).T

# Get vocabulary and co-occurrence matrix
vocab = vectorizer.get_feature_names_out()
co_occurrence_matrix = co_occurrence_matrix.toarray()

# Convert the co-occurrence matrix to a format suitable for GloVe
glove_input = {(vocab[i], vocab[j]): co_occurrence_matrix[i][j] for i in range(len(vocab)) for j in range(len(vocab))}

# Train the GloVe model
corpus = Corpus()
corpus.fit(glove_input, window=10)  # Adjust the window size as needed
glove_model = Glove(no_components=100, learning_rate=0.05)
glove_model.fit(corpus.matrix, epochs=100, no_threads=4, verbose=True)

# Example: Get the vector for the word "cat"
vector_cat = glove_model.word_vectors[glove_model.dictionary["cat"]]

# Example: Find similar words to "cat"
similar_words = glove_model.most_similar("cat", number=3)

# Display results
print("Vector for 'cat':", vector_cat)
print("Similar words to 'cat':", similar_words)
