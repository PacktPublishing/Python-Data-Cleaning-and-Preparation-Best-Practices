from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text
text = "Apple Inc. is planning to open a new store in New York City. The CEO, Tim Cook, announced the decision yesterday."

# Initialize NER pipeline
ner_pipeline = pipeline("ner")

# Perform NER on the text
ner_results = ner_pipeline(text)

# Extract named entities
named_entities = [entity['word'] for entity in ner_results if entity['entity'] != 'O']

# Tokenize the original text
tokens = word_tokenize(text)

# Remove stopwords based on identified entities
filtered_tokens = [token.lower() for token in tokens if token.lower() not in named_entities and token.lower() not in stopwords.words('english')]

# Print the results
print("Original Tokens:", tokens)
print("Filtered Tokens (After Stopword Removal based on Entities):", filtered_tokens)
