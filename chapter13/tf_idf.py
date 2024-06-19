from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "The cat in the hat.",
    "The hat on the cat."
]

# Create a TF-IDF model
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Calculate cosine similarity between the two documents
similarity_matrix_tfidf = cosine_similarity(tfidf_matrix)

# Get feature names (words)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Display the TF-IDF matrix
print("\nFeature Names:")
print(feature_names)
print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())
print("\nCosine Similarity Matrix (TF-IDF):")
print(similarity_matrix_tfidf)
