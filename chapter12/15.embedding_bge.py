from langchain_community.embeddings import HuggingFaceBgeEmbeddings

# Define the model name and parameters
model_name = "BAAI/bge-small-en"
model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}

# Initialize the embeddings model
bge_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# Sample sentences to embed
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "I love machine learning and natural language processing."
]

# Generate embeddings for each sentence
embeddings = [bge_embeddings.embed_query(sentence) for sentence in sentences]

# Print the embeddings
for i, embedding in enumerate(embeddings):
    print(f"Embedding for sentence {i+1}: {embedding[:5]}...")  # Print the first 5 values for brevity
    print(f"Length of embedding: {len(embedding)}")
