# from transformers import BertTokenizer, BertModel
# import sentencepiece as spm
# import torch

# # Training SentencePiece model
# corpus = "This is a sample sentence. Another sentence for training."
# spm.SentencePieceTrainer.Train('--input=corpus.txt --model_prefix=sp_model --vocab_size=50')

# # Load SentencePiece model and tokenizer
# sp_model = spm.SentencePieceProcessor()
# sp_model.Load("sp_model.model")
# bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# # Tokenize a sentence (simulating OOV word during testing)
# sentence = "This is a new word not seen during training."
# tokens = bert_tokenizer.tokenize(sentence)

# # Handle OOV words using SentencePiece
# encoded = sp_model.EncodeAsPieces(sentence)

# # Convert SentencePiece tokens to indices
# input_ids = bert_tokenizer.convert_tokens_to_ids(encoded)

# # Load pre-trained BERT model
# bert_model = BertModel.from_pretrained("bert-base-uncased")

# # Convert indices to PyTorch tensor
# input_ids_tensor = torch.tensor([input_ids])

# # Forward pass through BERT model
# outputs = bert_model(input_ids_tensor)

# # Print the original tokens, encoded tokens, and BERT model outputs
# print("Original Tokens:", tokens)
# print("Encoded Tokens:", encoded)
# print("BERT Model Outputs:", outputs)
