from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings

# Load the HuggingFace embedding model
embedding_model = HuggingFaceEmbeddings(model_name='roberta-base')

# Create a SemanticChunker with the correct parameters
text_splitter = SemanticChunker(
    embeddings=embedding_model,
    buffer_size=10,                                # Hypothetical buffer size
    add_start_index=True,                           # Whether to add start index for chunks
    breakpoint_threshold_type='interquartile',         # Type of breakpoint threshold
    breakpoint_threshold_amount=0.7,                # Amount for breakpoint threshold
    number_of_chunks=5                         # Target number of chunks, optional
)

# Example data
reviews = [
    "This smartphone has an excellent camera. The photos are sharp and the colors are vibrant. Overall, very satisfied with my purchase.",
    "I was disappointed with the laptop's performance. It frequently lags and the battery life is shorter than expected.",
    "The blender works great for making smoothies. It's powerful and easy to clean. Definitely worth the price.",
    "Customer support was unresponsive. I had to wait a long time for a reply, and my issue was not resolved satisfactorily.",
    "The book is a fascinating read. The storyline is engaging and the characters are well-developed. Highly recommend to all readers."
]

# Combine the reviews into a single text block for chunking
text_block = " ".join(reviews)

# Split the text into semantic chunks
chunks = text_splitter.split_text(text_block)

# Print the chunks
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}:")
    print(chunk.strip())
    print("-" * 50)
