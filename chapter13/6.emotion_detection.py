import torch
import pandas as pd
from transformers import WhisperProcessor, WhisperForConditionalGeneration, AutoModelForSequenceClassification, AutoTokenizer
import librosa
import numpy as np

# Load the Whisper processor and model from Hugging Face
whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
whisper_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# Load the emotion detection processor and model from Hugging Face
emotion_model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)

# Define the path to your audio file
audio_path = "chapter13/audio/3.chain orchestrator.mp3"  # Replace with your actual audio file path

# Load the audio file
audio, rate = librosa.load(audio_path, sr=16000)

# Function to split audio into chunks
def split_audio(audio, rate, chunk_duration=30):
    chunk_length = int(rate * chunk_duration)
    num_chunks = int(np.ceil(len(audio) / chunk_length))
    return [audio[i*chunk_length:(i+1)*chunk_length] for i in range(num_chunks)]

# Function to transcribe audio to text using Whisper
def transcribe_audio(audio_chunk, rate):
    # Preprocess the audio file for the Whisper model
    input_features = whisper_processor(audio_chunk, sampling_rate=rate, return_tensors="pt").input_features

    # Generate the transcription
    with torch.no_grad():
        predicted_ids = whisper_model.generate(input_features)

    # Decode the generated transcription
    transcription = whisper_processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription

# Function to detect emotions from text using the emotion detection model
def detect_emotion(text):
    inputs = emotion_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = emotion_model(**inputs)
    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
    emotions = emotion_model.config.id2label
    return emotions[predicted_class_id]

# Split audio into chunks
audio_chunks = split_audio(audio, rate, chunk_duration=30)  # 30-second chunks

# Create a DataFrame to store results
df = pd.DataFrame(columns=['Chunk Index', 'Transcription', 'Emotion'])

# Process each audio chunk
for i, audio_chunk in enumerate(audio_chunks):
    transcription = transcribe_audio(audio_chunk, rate)
    emotion = detect_emotion(transcription)
    
    # Append results to DataFrame
    df.loc[i] = [i, transcription, emotion]
    print(f"Processed Chunk {i+1}/{len(audio_chunks)}")

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('transcriptions_with_emotions.csv', index=False)
