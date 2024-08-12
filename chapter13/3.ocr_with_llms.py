import pandas as pd
import json
import re
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub

# Read the CSV file
df = pd.read_csv('extracted_texts.csv')

# Initialize the Hugging Face model
model_name = "mistralai/Mistral-Nemo-Instruct-2407"  # Using Mistral for instruction-following

# Your Hugging Face API token
api_token = "add_your_token"  # Replace with your actual API token

# LangChain setup with few-shot examples
prompt_template = PromptTemplate(
    input_variables=["text"],
    template='''Correct the following text for spelling errors and return only the corrected text in lowercase. Respond using JSON format, strictly according to the following schema:
{{"corrected_text": "corrected text in lowercase"}}

Examples:
Input: "Open vs Proprietry LLMs"
Output: {{"corrected_text": "open vs proprietary llms"}}

Input: "HOW TO MITIGATE SaCURITY RISKS IN AI AND ML SYSTEM VECTOR LAB"
Output: {{"corrected_text": "how to mitigate security risks in ai and ml system vector lab"}}

Input: "BUILDING DBRX-CLASS CUSTOM LLMS WITH MOSAIC A1 TRAINING VECTOR LAB"
Output: {{"corrected_text": "building dbrx-class custom llms with mosaic a1 training vector lab"}}

Text to correct:
{text}
Output (JSON format only):
'''
)

huggingface_llm = HuggingFaceHub(repo_id=model_name, huggingfacehub_api_token=api_token, model_kwargs={"task": "text-generation"})
llm_chain = LLMChain(prompt=prompt_template, llm=huggingface_llm)

def correct_text(text):
    # Use the LLMChain to generate a response
    response = llm_chain.run(text)
    print(f"Raw Response: {response}")  # Debugging line to see the raw response

    # Use regex to extract the JSON part that follows "Output (JSON format only):"
    json_match = re.search(r'Output \(JSON format only\):\s*(\{.*\})', response)
    if json_match:
        json_str = json_match.group(1)
        try:
            response_json = json.loads(json_str)
            corrected_text = response_json.get('corrected_text', '')
            return corrected_text
        except json.JSONDecodeError as json_error:
            print(f"JSON Decode Error: {json_error}")
            return "error"
    else:
        print("No valid JSON object found in the response")
        return "error"

# Apply text correction to the 'Extracted Text' column
df['Corrected Text'] = df['Extracted Text'].apply(correct_text)

# Display the DataFrame
print(df)

# Optionally, save the updated DataFrame to a new CSV file
df.to_csv('cleaned_texts.csv', index=False)

# Print examples of corrections
for _, row in df.iterrows():
    print("Original:", row['Extracted Text'])
    print("Corrected:", row['Corrected Text'])
    print()
