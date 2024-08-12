import os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from transformers import BlipProcessor, BlipForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub

# Define the folder containing images
folder_path = 'chapter13/images'

# Supported image extensions
supported_extensions = ('.png', '.jpg', '.jpeg')

# Get all images in the folder
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(supported_extensions)]

# Create an empty DataFrame to store results
df = pd.DataFrame(columns=['Image Path', 'Generated Caption', 'Refined Caption'])

# Initialize the BLIP model and processor for image captioning
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

# Initialize the LLM for text refinement
llm_model_name = "google/flan-t5-small"  # You can choose other models as well
tokenizer = AutoTokenizer.from_pretrained(llm_model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(llm_model_name)

# LangChain setup
api_token = ""
prompt_template = PromptTemplate(input_variables=["text"], template="Refine and correct the following caption: {text}")
huggingface_llm = HuggingFaceHub(repo_id=llm_model_name, huggingfacehub_api_token=api_token)
llm_chain = LLMChain(prompt=prompt_template, llm=huggingface_llm)

def refine_caption(caption):
    # Create a prompt using LangChain and generate refined caption
    prompt = prompt_template.format(text=caption)
    refined_caption = llm_chain.run(prompt)
    return refined_caption

def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = blip_processor(images=image, return_tensors="pt")
    outputs = blip_model.generate(**inputs)
    caption = blip_processor.decode(outputs[0], skip_special_tokens=True)
    return caption

# Process each image in the folder
if not image_paths:
    print("No images found in the specified folder.")
else:
    for image_path in image_paths:
        # Generate image caption
        caption = generate_caption(image_path)
        print(f"Generated Caption for {os.path.basename(image_path)}:\n{caption}\n")
        
        # Refine the caption
        refined_caption = refine_caption(caption)
        print(f"Refined Caption:\n{refined_caption}\n")
        
        # Append results to DataFrame
        df.loc[len(df)] = [image_path, caption, refined_caption]

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('captions.csv', index=False)
