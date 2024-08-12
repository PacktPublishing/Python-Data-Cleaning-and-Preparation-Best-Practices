from PIL import Image
import numpy as np
import cv2
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Function to display images
def show_image(image, title="Image"):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load image from a URL
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Example image URL from Unsplash (open-source image)
image_url = "https://images.unsplash.com/photo-1593642532871-8b12e02d091c"
image = load_image_from_url(image_url)

print("Loaded Image from URL")
# Display the original image
show_image(image, "Original Image")

def resize_and_crop(image, target_size):
    # Resize image
    image = image.resize((target_size, target_size), Image.LANCZOS)
    return image

target_size = 256
processed_image = resize_and_crop(image, target_size)

# Display the processed image
show_image(processed_image, "Resized and Cropped Image")

def normalize(image):
    # Convert image to numpy array
    image_array = np.array(image)
    # Normalize pixel values to range [0, 1]
    normalized_array = image_array / 255.0
    return normalized_array

def standardize(image):
    # Convert image to numpy array
    image_array = np.array(image)
    # Calculate the mean and standard deviation
    mean = np.mean(image_array, axis=(0, 1), keepdims=True)
    std = np.std(image_array, axis=(0, 1), keepdims=True)
    # Standardize pixel values
    standardized_array = (image_array - mean) / std
    return standardized_array

# Normalize the processed image
normalized_image = normalize(processed_image)

# Display the normalized image
show_image(normalized_image, "Normalized Image")

# Standardize the processed image
standardized_image = standardize(processed_image)

# Display the standardized image
show_image(standardized_image, "Standardized Image")

# Verify standardization by checking mean and standard deviation
mean_after = np.mean(standardized_image)
std_after = np.std(standardized_image)
print(f"Mean after standardization: {mean_after}")
print(f"Standard deviation after standardization: {std_after}")

# Ensure that the mean and standard deviation are within the expected range
assert np.isclose(mean_after, 0, atol=1e-6), "Standardization failed: mean is not close to 0"
assert np.isclose(std_after, 1, atol=1e-6), "Standardization failed: standard deviation is not close to 1"
print("Standardization completed successfully.")

# Define an image data generator for augmentation
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Function to apply augmentation and visualize the result
def augment_image(image):
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    augmented_iter = datagen.flow(image, batch_size=1)
    augmented_image = next(augmented_iter)[0]
    return augmented_image

augmented_image = augment_image(normalized_image)

# Display the augmented image
show_image(augmented_image, "Augmented Image")

# Convert image to tensor
tensor_image = tf.convert_to_tensor(augmented_image, dtype=tf.float32)

# Convert back to image format to visualize
def tensor_to_image(tensor):
    tensor = tensor.numpy()
    tensor = np.clip(tensor, 0, 1)  # Clip values to [0, 1]
    return tensor

# Function to add salt-and-pepper noise to an image
def add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    noisy_image = np.copy(image)
    # Salt noise
    num_salt = np.ceil(salt_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 1

    # Pepper noise
    num_pepper = np.ceil(pepper_prob * image.size)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1], :] = 0

    return noisy_image

# Flag to control whether to add salt and pepper noise
use_salt_and_pepper_noise = False

if use_salt_and_pepper_noise:
    # Add salt-and-pepper noise to the augmented image
    noisy_image = add_salt_and_pepper_noise(tensor_to_image(tensor_image))

    # Display the noisy image
    show_image(noisy_image, "Salt-and-Pepper Noisy Image")
else:
    # No noise applied, use the original image for denoising
    noisy_image = tensor_to_image(tensor_image)
    show_image(noisy_image, "Original Image (No Noise)")

# Function to remove noise using Gaussian Blur
def gaussian_blur(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

# Function to remove noise using Median Blur
def median_blur(image):
    image_uint8 = (image * 255).astype(np.uint8)
    blurred_image = cv2.medianBlur(image_uint8, 5)
    blurred_image = blurred_image / 255.0
    return blurred_image

# Function to remove noise using Bilateral Filter
def bilateral_filter(image):
    image_uint8 = (image * 255).astype(np.uint8)
    filtered_image = cv2.bilateralFilter(image_uint8, 9, 75, 75)
    filtered_image = filtered_image / 255.0
    return filtered_image

# Function to remove noise using Non-Local Means Denoising
def remove_noise(image):
    image_uint8 = (image * 255).astype(np.uint8)
    denoised_image = cv2.fastNlMeansDenoisingColored(image_uint8, None, h=10, templateWindowSize=7, searchWindowSize=21)
    denoised_image = denoised_image / 255.0
    return denoised_image

# Apply and display denoising techniques
blurred_image = gaussian_blur(noisy_image)
show_image(blurred_image, "Gaussian Blur")

median_blurred_image = median_blur(noisy_image)
show_image(median_blurred_image, "Median Blur")

bilateral_filtered_image = bilateral_filter(noisy_image)
show_image(bilateral_filtered_image, "Bilateral Filter")

denoised_image = remove_noise(noisy_image)
show_image(denoised_image, "Non-Local Means Denoising")
