import torch
import pandas as pd
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import numpy as np
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub

# Load the Whisper processor and model from Hugging Face
whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
whisper_model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# Initialize the Hugging Face model
model_name = "mistralai/Mistral-Nemo-Instruct-2407"  # Using Mistral for instruction-following

# Your Hugging Face API token
api_token = "add_your_huggigng_face_token"  # Replace with your actual API token

# LangChain setup with few-shot examples
prompt_template = PromptTemplate(
    input_variables=["text"],
    template='''This is the transcribed text from a YouTube video. Write the key highlights from this video in bullet format.
{text}
Output:
'''
)

huggingface_llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=api_token, model_kwargs={"task": "text-generation"})
llm_chain = LLMChain(prompt=prompt_template, llm=huggingface_llm)

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

# Function to generate key highlights from text using the LLM
def generate_highlights(text):
    try:
        response = llm_chain.run(text)
        return response.strip()  # Clean up any whitespace around the response
    except Exception as e:
        print(f"Error generating highlights: {e}")
        return "error"  # Handle errors gracefully

# Split audio into chunks
audio_chunks = split_audio(audio, rate, chunk_duration=30)  # 30-second chunks

# Transcribe each audio chunk
transcriptions = [transcribe_audio(chunk, rate) for chunk in audio_chunks]

# Join all transcriptions into a single text
full_transcription = " ".join(transcriptions)

# Generate highlights from the full transcription
highlights = generate_highlights(full_transcription)

# Create a DataFrame to store results
df = pd.DataFrame(columns=['Full Transcription', 'Highlights'])
df.loc[0] = [full_transcription, highlights]

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('transcriptions_with_highlights.csv', index=False)

# Print examples of corrections
print("Full Transcription:", full_transcription)
print("Highlights:", highlights)
