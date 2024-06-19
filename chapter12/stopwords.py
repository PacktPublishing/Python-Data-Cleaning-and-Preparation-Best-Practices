from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

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
    
    # Stopword Removal using NLTK
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in word_tokens if word.lower() not in stop_words]
    
    print("   Word Tokens (Before Stopword Removal):", word_tokens)
    print("   Word Tokens (After Stopword Removal):", filtered_tokens)
