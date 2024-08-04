import nltk
from nltk.tokenize import word_tokenize

# Download the necessary NLTK data (run this once)
nltk.download('punkt')

# Sample text
text = "The quick brown fox jumps over the lazy dog. It's unaffordable!"

# Perform word tokenization
word_tokens = word_tokenize(text)

print("Word tokens:")
print(word_tokens)