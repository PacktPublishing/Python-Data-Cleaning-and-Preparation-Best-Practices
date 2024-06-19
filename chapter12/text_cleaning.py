from bs4 import BeautifulSoup
from transformers import BertTokenizer

# Sample user reviews
reviews = [
    "<html>This product    is <b>amazing!</b></html>",
    "The product is good, but it could be better!!!",
    "I've never seen such a terrible      product. 0/10",
    "The product is AWESOME!!! Highly recommended!",
]

# a. Removing HTML tags and Special Characters
def clean_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# b. Handling Capitalization and Letter Case
def standardize_case(text):
    return text.lower()

# c. Dealing with Numerical Values and Symbols
def remove_numbers_and_symbols(text):
    return ''.join(e for e in text if e.isalpha() or e.isspace())

# d. Addressing Whitespace and Formatting Issues
def remove_extra_whitespace(text):
    return ' '.join(text.split())


# Applying the text preprocessing pipeline
def preprocess_text(text):
    text = clean_html_tags(text)
    text = standardize_case(text)
    text = remove_numbers_and_symbols(text)
    text = remove_extra_whitespace(text)
    return text

# Preprocess all reviews
preprocessed_reviews = [preprocess_text(review) for review in reviews]

print("Original Reviews:")
for review in reviews:
    print(f"- {review}")

print("\nPreprocessed Reviews:")
for preprocessed_review in preprocessed_reviews:
    print(f"- {preprocessed_review}")

