import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa

# Load the Whisper processor and model from Hugging Face
processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# Define the path to your audio file
audio_path = "chapter13/audio/3.chain orchestrator.mp3"  # Replace with your actual audio file path

# Load the audio file
audio, rate = librosa.load(audio_path, sr=16000)

# Preprocess the audio file for the Whisper model
input_features = processor(audio, sampling_rate=rate, return_tensors="pt").input_features

# Generate the transcription
with torch.no_grad():
    predicted_ids = model.generate(input_features)

# Decode the generated transcription
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

# Print the transcribed text
print("Transcribed Text:")
print(transcription)
