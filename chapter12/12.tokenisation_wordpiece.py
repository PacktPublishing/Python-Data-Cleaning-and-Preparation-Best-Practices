from transformers import BertTokenizer 

# Load the pre-trained tokenizer 
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased') 

# Sample text 
text = "Tokenization in medical texts can include words like hyperlipidemia." 


# Tokenize the text 
tokens = tokenizer.tokenize(text) 
print("Tokens:", tokens) 

# Convert tokens to input IDs 
input_ids = tokenizer.convert_tokens_to_ids(tokens) 
print("Input IDs:", input_ids) 