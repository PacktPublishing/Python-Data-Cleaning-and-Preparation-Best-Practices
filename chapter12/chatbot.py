from fuzzywuzzy import fuzz
from spellchecker import SpellChecker

# Sample predefined correction rules
correction_rules = {
    "u": "you",
    "gr8": "great",
    "2moro": "tomorrow",
    "b4": "before",
    "lol": "laugh out loud",
}

def correct_spelling(query):
    # Split the query into words
    words = query.split()

    # Apply predefined correction rules
    corrected_words = [correction_rules.get(word, word) for word in words]

    # Join the corrected words back into a sentence
    corrected_query = " ".join(corrected_words)

    return corrected_query

# Sample user queries with potential spelling mistakes
user_queries = [
    "u there?",
    "gr8 job!",
    "let's meet 2moro",
    "b4 we go, lol",
]

# Create a SpellChecker instance for additional correction
spell_checker = SpellChecker()

# Correct spelling variations during post-processing
for user_query in user_queries:
    # Step 1: Apply predefined correction rules
    corrected_query = correct_spelling(user_query)

    # Step 2: Use spell-checking for additional correction
    corrected_query = " ".join([spell_checker.correction(word) for word in corrected_query.split()])

    # Print the original and corrected queries
    print("Original Query:", user_query)
    print("Corrected Query:", corrected_query)
    print("-" * 30)
