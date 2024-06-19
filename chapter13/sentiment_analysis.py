from transformers import BertTokenizer, BertModel
import torch
from nltk.corpus import movie_reviews

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Load the nltk movie reviews dataset
movie_reviews_dataset = [(movie_reviews.raw(fileid), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]

def analyze_review_sentiment(review_text):
    # Tokenize and encode the review text
    tokens = tokenizer(review_text, return_tensors="pt")

    # Obtain BERT embeddings
    with torch.no_grad():
        embeddings = model(**tokens).last_hidden_state

    # Calculate average embeddings for the entire review
    avg_embedding = torch.mean(embeddings, dim=1).squeeze().numpy()

    # Perform sentiment analysis using the embeddings (you can use a classifier here)
    # For simplicity, let's consider a threshold for positive and negative sentiment
    sentiment = "positive" if avg_embedding.mean() > 0 else "negative"

    return {"review": review_text, "sentiment": sentiment}

# Example: Analyzing sentiment of movie reviews
reviews_to_analyze = [review_text for review_text, _ in movie_reviews_dataset[:5]]

# Analyze sentiment for each review
for review_text in reviews_to_analyze:
    result = analyze_review_sentiment(review_text)
    print(result)

