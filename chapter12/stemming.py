from transformers import BertTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

import nltk
nltk.download('wordnet')

# Sample reviews
reviews = [
    "<html>This product is <b>amazing!</b></html>",
    "The product is good, but it could be better!!!",
    "I've never seen such a terrible product. 0/10",
    "The product is AWESOME!!! Highly recommended!",
]

# Combine the reviews into a single corpus
corpus = ' '.join(reviews)

# Initialize the BERT tokenizer
bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the corpus using BERT tokenizer
tokens = bert_tokenizer.tokenize(corpus)

# Initialize stemming and lemmatization tools
porter_stemmer = PorterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# Perform stemming and lemmatization
stemmed_tokens = [porter_stemmer.stem(token.lower()) for token in tokens]
lemmatized_tokens = [wordnet_lemmatizer.lemmatize(token.lower()) for token in tokens]

# Print the results
print("Original Tokens:", tokens)
print("\nStemmed Tokens:", stemmed_tokens)
print("\nLemmatized Tokens:", lemmatized_tokens)
