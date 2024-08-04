from tokenizers import Tokenizer

# Load the pre-trained GPT-2 BPE tokenizer
tokenizer = Tokenizer.from_pretrained("gpt2")

# Sample text
text = "Tokenization in medical texts can include words like hyperlipidemia.."

# Tokenize the text
encoding = tokenizer.encode(text)

# Print the tokens
print("Tokens:", encoding.tokens)

# Print the token IDs
print("Token IDs:", encoding.ids)

# Decode the token IDs back to text
decoded_text = tokenizer.decode(encoding.ids)
print("Decoded Text:", decoded_text)