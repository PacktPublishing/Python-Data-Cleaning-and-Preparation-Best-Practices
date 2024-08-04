from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
import os

reviews = [
    "This smartphone has an excellent camera. The photos are sharp and the colors are vibrant. Overall, very satisfied with my purchase.",
    "I was disappointed with the laptop's performance. It frequently lags and the battery life is shorter than expected.",
    "The blender works great for making smoothies. It's powerful and easy to clean. Definitely worth the price.",
    "Customer support was unresponsive. I had to wait a long time for a reply, and my issue was not resolved satisfactorily.",
    "The book is a fascinating read. The storyline is engaging and the characters are well-developed. Highly recommend to all readers."
]
# Combine the reviews into a single text block for chunking
text_block = " ".join(reviews)

text_splitter = SemanticChunker(HuggingFaceEmbeddings())

docs = text_splitter.create_documents([text_block])

for i, doc in enumerate(docs):
    print(f"Chunk {i + 1}:")
    print(doc.page_content)
    print("\n")