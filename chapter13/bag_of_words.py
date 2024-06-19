from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "The cat in the hat.",
    "The hat on the cat."
]

# Create a Bag of Words model
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

# Get feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Calculate cosine similarity between the two documents
similarity_matrix = cosine_similarity(bow_matrix)

# Display the Bag of Words matrix
print("Bag of Words Matrix:")
print(bow_matrix.toarray())
print("\nFeature Names:")
print(feature_names)
print("\nCosine Similarity Matrix:")
print(similarity_matrix)
