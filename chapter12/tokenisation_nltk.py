import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# Sample user reviews
reviews = [
    "<html>This product is <b>amazing!</b></html>",
    "The product is good, but it could be better!!!",
    "I've never seen such a terrible product. 0/10",
    "The product is AWESOME!!! Highly recommended!",
]

# Iterate through each review
for i, review in enumerate(reviews, 1):
    print(f"\nReview {i}: {review}")

    # Word Tokenization using NLTK
    word_tokens = word_tokenize(review)
    print("   Word Tokens:", word_tokens)
