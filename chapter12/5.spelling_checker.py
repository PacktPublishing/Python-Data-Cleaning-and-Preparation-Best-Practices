from transformers import pipeline

def fix_spelling(text):
    # Initialize the spelling correction pipeline
    spell_check = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")
    
    # Generate the corrected text
    corrected = spell_check(text, max_length=2048)[0]['generated_text']
    
    return corrected

# Test the function with some sample text containing spelling mistakes
sample_text = "y name si from Grece."
corrected_text = fix_spelling(sample_text)

print("Original text:", sample_text)
print("Corrected text:", corrected_text)