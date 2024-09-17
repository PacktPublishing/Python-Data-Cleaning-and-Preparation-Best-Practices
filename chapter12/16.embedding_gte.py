from sentence_transformers import SentenceTransformer

# Load the GTE-base model
model = SentenceTransformer('thenlper/gte-base')

# Sample texts to embed
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "I love machine learning and natural language processing.",
    "Embeddings are useful for many NLP tasks."
]

# Generate embeddings
embeddings = model.encode(texts)

# Print the shape of the embeddings
print(f"Shape of embeddings: {embeddings.shape}")

# Print the first few values of the first embedding
print(f"First few values of the first embedding: {embeddings[0][:5]}")
