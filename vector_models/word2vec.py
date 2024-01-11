from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# Sample documents
documents = [
    "The cat in the hat and the cats in the car",
    "The hat on the cat and the kitten in the car"
]

# Tokenize the documents
tokenized_documents = [word_tokenize(doc.lower()) for doc in documents]

# Train a Word2Vec model
word2vec_model = Word2Vec(sentences=tokenized_documents, vector_size=100, window=5, min_count=1, workers=4)

# Get the vector for a specific word
vector_cat = word2vec_model.wv["cat"]

# Find similar words to "cat"
similar_words = word2vec_model.wv.most_similar("cat", topn=10)

# Display results
print("Vector for 'cat':", vector_cat)
print("Similar words to 'cat':", similar_words)
