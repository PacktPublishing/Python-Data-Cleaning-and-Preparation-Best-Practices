import string

# Sample text
text = "I love this product!!! It's amazing!!!"

# Option 1: Retain symbols and punctuation
retained_text = "".join(char for char in text if char.isalnum() or char.isspace())
print("Retained Text:", retained_text)

# Option 2: Replace symbols and punctuation
replaced_text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
print("Replaced Text:", replaced_text)

# Option 3: Remove symbols and punctuation
removed_text = "".join(char for char in text if char.isalnum() or char.isspace())
print("Removed Text:", removed_text)
