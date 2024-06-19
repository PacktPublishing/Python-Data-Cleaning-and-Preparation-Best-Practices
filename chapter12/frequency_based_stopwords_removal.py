from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import word_tokenize

# Sample user reviews
reviews = [
    "<html>This product is <b>amazing!</b></html>",
    "The product is good, but it could be better!!!",
    "I've never seen such a terrible product. 0/10",
    "The product is AWESOME!!! Highly recommended!",
]

# Combine the reviews into a single corpus
corpus = ' '.join(reviews)

# Tokenize the corpus
tokens = word_tokenize(corpus)

# Calculate word frequencies
freq_dist = FreqDist(tokens)

# Set a threshold for the frequency to consider as a stopword (adjust as needed)
frequency_threshold = 2

# Identify stopwords based on frequency
stopwords_by_frequency = {word for word, freq in freq_dist.items() if freq > frequency_threshold}

# Use NLTK's English stopwords
nltk_stopwords = set(stopwords.words('english'))

# Combined stopwords set (frequency-based + NLTK stopwords)
all_stopwords = nltk_stopwords.union(stopwords_by_frequency)

# Remove stopwords from the tokenized corpus
filtered_tokens = [word for word in tokens if word.lower() not in all_stopwords]

# Display the results
print("Original Tokens:", tokens)
print("Filtered Tokens (After Stopword Removal):", filtered_tokens)
