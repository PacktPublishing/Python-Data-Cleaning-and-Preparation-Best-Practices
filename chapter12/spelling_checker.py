from transformers import BertTokenizer
from spellchecker import SpellChecker

# Load pre-trained BERT tokenizer
bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize a sentence with a typo
sentence = "I love to reaed bbooks."
tokens = bert_tokenizer.tokenize(sentence)

# Implement spell-checking mechanism
spell_checker = SpellChecker()
corrected_tokens = [spell_checker.correction(token) for token in tokens]

# Print the original tokens and corrected tokens
print("Original Tokens:", tokens)
print("Corrected Tokens:", corrected_tokens)
