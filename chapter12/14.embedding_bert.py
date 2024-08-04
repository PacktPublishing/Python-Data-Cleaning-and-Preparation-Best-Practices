# Import necessary libraries
from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Input sentence
sentence = "BERT embeddings are very useful for natural language processing tasks."

# Tokenize the input sentence
inputs = tokenizer(sentence, return_tensors='pt')

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract the last hidden states (embeddings)
last_hidden_states = outputs.last_hidden_state

# Print the shape of the embeddings tensor
print("Shape of the embeddings tensor:", last_hidden_states.shape)

# Print the embeddings for the first token (CLS token)
cls_embedding = last_hidden_states[0, 0, :].numpy()
print("CLS token embedding:", cls_embedding)

# Print the embeddings for the first word
first_word_embedding = last_hidden_states[0, 1, :].numpy()
print("First word embedding:", first_word_embedding)
