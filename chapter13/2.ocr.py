import os
import pandas as pd
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Define the folder containing images
folder_path = 'chapter13/images'

# Supported image extensions
supported_extensions = ('.png', '.jpg', '.jpeg')

# Get all images in the folder
image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(supported_extensions)]

# Create an empty DataFrame to store results
df = pd.DataFrame(columns=['Image Path', 'Extracted Text'])

# Check if there are any images found
if not image_paths:
    print("No images found in the specified folder.")
else:
    # Function to process images and extract text
    def process_image(image_path):
        # Perform OCR on the image
        result = ocr.ocr(image_path, cls=True)
        
        # Extracting and printing the text
        extracted_text = ""
        for line in result[0]:
            extracted_text += line[1][0] + " "
        print(f"Extracted Text from {os.path.basename(image_path)}:\n{extracted_text}\n")
        
        # Append results to DataFrame
        df.loc[len(df)] = [image_path, extracted_text]

    # Process each image in the folder
    for image_path in image_paths:
        process_image(image_path)

# Display the DataFrame
print(df)

# Optionally, save the DataFrame to a CSV file
df.to_csv('extracted_texts.csv', index=False)
