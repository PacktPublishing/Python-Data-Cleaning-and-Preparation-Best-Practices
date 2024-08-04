# Step 1: Load Example Data
reviews = [
    "This smartphone has an excellent camera. The photos are sharp and the colors are vibrant. Overall, very satisfied with my purchase.",
    "I was disappointed with the laptop's performance. It frequently lags and the battery life is shorter than expected.",
    "The blender works great for making smoothies. It's powerful and easy to clean. Definitely worth the price.",
    "Customer support was unresponsive. I had to wait a long time for a reply, and my issue was not resolved satisfactorily.",
    "The book is a fascinating read. The storyline is engaging and the characters are well-developed. Highly recommend to all readers."
]

# Step 2: Create the TokenTextSplitter
from langchain_text_splitters import TokenTextSplitter

# Initialize the TokenTextSplitter with a chunk size of 50 tokens and no overlap
text_splitter = TokenTextSplitter(chunk_size=50, chunk_overlap=0)

# Step 3: Join Reviews and Split Text
# Combine the reviews into a single text block for chunking
text_block = " ".join(reviews)

# Split the text into token-based chunks
chunks = text_splitter.split_text(text_block)

# Print the chunks
print("Chunks with 50 tokens each:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}:")
    print(chunk)
    print("\n")

# Step 4: Experiment with Different Chunk Sizes
chunk_sizes = [20, 70, 150]

for size in chunk_sizes:
    print(f"Chunk Size: {size}")
    text_splitter = TokenTextSplitter(chunk_size=size, chunk_overlap=0)
    chunks = text_splitter.split_text(text_block)
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:")
        print(chunk)
        print("\n")
