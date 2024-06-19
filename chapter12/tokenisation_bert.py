from transformers import BertTokenizer

# Sample user reviews
reviews = [
    "<html>This product is <b>amazing!</b></html>",
    "The product is good, but it could be better!!!",
    "I've never seen such a terrible product. 0/10",
    "The product is AWESOME!!! Highly recommended!",
]

# Initialize BERT tokenizer
bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Iterate through each review
for i, review in enumerate(reviews, 1):
    print(f"\nReview {i}: {review}")

    # b. Subword Tokenization
    subword_tokens = bert_tokenizer.tokenize(review)
    print("   Subword Tokens:", subword_tokens)

    # a. Word Tokenization
    word_tokens = bert_tokenizer.encode(review, add_special_tokens=False)
    word_tokens = bert_tokenizer.convert_ids_to_tokens(word_tokens)
    print("   Word Tokens:", word_tokens)

    # c. Character Tokenization
    char_tokens = list(review)
    print("   Character Tokens:", char_tokens)
