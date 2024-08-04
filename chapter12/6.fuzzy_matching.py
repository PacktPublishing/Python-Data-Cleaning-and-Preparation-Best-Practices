from transformers import pipeline
from thefuzz import process, fuzz

def fix_spelling(text, threshold=80):
    # Initialize the spelling correction pipeline
    spell_check = pipeline("text2text-generation", model="oliverguhr/spelling-correction-english-base")
    
    # Generate the corrected text
    corrected = spell_check(text, max_length=2048)[0]['generated_text']
    
    # Split the original and corrected texts into words
    original_words = text.split()
    corrected_words = corrected.split()
    
    # Create a dictionary of common English words (you can expand this list)
    common_words = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at'])
    
    # Fuzzy match each word
    final_words = []
    for orig, corr in zip(original_words, corrected_words):
        if orig.lower() in common_words:
            final_words.append(orig)  # Keep common words as they are
        else:
            # Use fuzzy matching to find the best match
            matches = process.extractOne(orig, [corr], scorer=fuzz.ratio)
            if matches[1] >= threshold:
                final_words.append(matches[0])
            else:
                final_words.append(orig)  # Keep the original word if no good match found
    
    return ' '.join(final_words)

# Test the function with some sample text containing spelling mistakes
sample_text = "Lets do a copmarsion of speling mistaks in this sentense."
corrected_text = fix_spelling(sample_text)

print("Original text:", sample_text)
print("Corrected text:", corrected_text)