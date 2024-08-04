import stanza
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from collections import Counter
import numpy as np
import torch

# Initialize Stanza for biomedical text
stanza.download('en', package='mimic', processors='tokenize')
nlp = stanza.Pipeline('en', package='mimic', processors='tokenize')

# Initialize standard GPT-2 tokenizer
standard_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
standard_tokenizer.pad_token = standard_tokenizer.eos_token  # Set pad_token to eos_token
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.config.pad_token_id = model.config.eos_token_id  # Set pad_token_id for the model

# Sample medical corpus
corpus = [
    "The patient suffered a myocardial infarction.",
    "Early detection of heart attack is crucial.",
    "Treatment for myocardial infarction includes medication.",
    "Patients with heart conditions require regular check-ups.",
    "Myocardial infarction can lead to severe complications."
]

def stanza_tokenize(text):
    doc = nlp(text)
    tokens = [word.text for sent in doc.sentences for word in sent.words]
    return tokens

def calculate_oov_and_compression(corpus, tokenizer):
    oov_count = 0
    total_tokens = 0
    all_tokens = []

    for sentence in corpus:
        tokens = tokenizer.tokenize(sentence) if hasattr(tokenizer, 'tokenize') else stanza_tokenize(sentence)
        all_tokens.extend(tokens)
        total_tokens += len(tokens)
        oov_count += tokens.count(tokenizer.oov_token) if hasattr(tokenizer, 'oov_token') else 0

    oov_rate = (oov_count / total_tokens) * 100 if total_tokens > 0 else 0
    avg_tokens_per_sentence = total_tokens / len(corpus)

    return oov_rate, avg_tokens_per_sentence, all_tokens

def analyze_token_utilization(tokens):
    token_counts = Counter(tokens)
    total_tokens = len(tokens)
    utilization = {token: count / total_tokens for token, count in token_counts.items()}
    return utilization

def calculate_perplexity(tokenizer, model, text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
    return torch.exp(outputs.loss).item()

# Evaluation
for tokenizer_name, tokenizer in [("Standard GPT-2", standard_tokenizer), ("Stanza Medical", stanza_tokenize)]:
    oov_rate, avg_tokens, all_tokens = calculate_oov_and_compression(corpus, tokenizer)
    utilization = analyze_token_utilization(all_tokens)
    
    print(f"\n{tokenizer_name} Tokenizer:")
    print(f"OOV Rate: {oov_rate:.2f}%")
    print(f"Average Tokens per Sentence: {avg_tokens:.2f}")
    print("Top 5 Most Used Tokens:")
    for token, freq in sorted(utilization.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {token}: {freq:.2%}")
    

# Example output for "myocardial infarction"
term = "myocardial infarction"
print(f"\nTokenizing '{term}':")
print(f"Standard GPT-2: {standard_tokenizer.tokenize(term)}")
print(f"Stanza Medical: {stanza_tokenize(term)}")