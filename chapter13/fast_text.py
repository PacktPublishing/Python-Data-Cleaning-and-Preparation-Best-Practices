import nltk
from nltk.corpus import movie_reviews

# Download the IMDb movie reviews dataset
nltk.download('movie_reviews')

import fasttext
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
import random

# Load positive and negative movie reviews from the IMDb dataset
positive_reviews = [(movie_reviews.raw(fileid), '__label__pos') for fileid in movie_reviews.fileids('pos')]
negative_reviews = [(movie_reviews.raw(fileid), '__label__neg') for fileid in movie_reviews.fileids('neg')]

# Combine positive and negative reviews and shuffle them
all_reviews = positive_reviews + negative_reviews
random.shuffle(all_reviews)

# Tokenize the reviews
tokenized_reviews = [word_tokenize(review.lower()) for (review, label) in all_reviews]

# Create a training text file for FastText
with open("fasttext_movie_reviews_train.txt", "w") as f:
    for (review, label) in all_reviews:
        f.write(f"{label} {' '.join(word_tokenize(review.lower()))}\n")

# Train the FastText model
model = fasttext.train_unsupervised("fasttext_movie_reviews_train.txt", model="skipgram", dim=100, epoch=100, lr=0.05, minCount=1)

# Example: Get the vector for the word "movie"
vector_movie = model["movie"]

# Example: Find similar words to "movie"
similar_words = model.get_nearest_neighbors("movie", k=3)

# Display results
print("Vector for 'movie':", vector_movie)
print("Similar words to 'movie':", similar_words)
