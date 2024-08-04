from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define a text prompt with a rare word
text = "The quokka, a rare marsupial,"

# Encode the input text to tensor
indexed_tokens = tokenizer.encode(text, return_tensors='pt')

# Generate text until the output length reaches 50 tokens
output_text = model.generate(indexed_tokens, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

# Decode the output text
output_text_decoded = tokenizer.decode(output_text[0], skip_special_tokens=True)
print(output_text_decoded)