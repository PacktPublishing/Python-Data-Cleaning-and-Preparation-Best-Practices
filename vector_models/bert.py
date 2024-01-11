from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Encode input text
input_text = "BERT embeddings capture contextual information."
tokens = tokenizer(input_text, return_tensors="pt")

# Obtain BERT embeddings
with torch.no_grad():
    embeddings = model(**tokens).last_hidden_state

# Use embeddings for downstream tasks or analysis
print(embeddings)
