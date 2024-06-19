import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Create a dataset with features related to housing prices
np.random.seed(42)
num_samples = 100

# Square footage in square feet
square_footage = np.random.uniform(500, 5000, num_samples)

# Distance to the nearest school in miles
distance_to_school = np.random.uniform(0.1, 5, num_samples)

# Commute distance to work in miles
commute_distance = np.random.exponential(5, num_samples)

# Traffic density (skewed feature)
traffic_density = np.random.exponential(2, num_samples)

# Create a DataFrame
data = pd.DataFrame({
    'Square_Footage': square_footage,
    'Distance_to_School': distance_to_school,
    'Commute_Distance': commute_distance,
    'Traffic_Density': traffic_density
})


# Display original dataset statistics
print("Original Dataset Statistics:")
print(data.describe())

# Plot the distributions before scaling
plt.figure(figsize=(12, 8))

for i, column in enumerate(data.columns):
    plt.subplot(2, 2, i+1)
    plt.title(f"Distribution of '{column}' Before Scaling")
    plt.hist(data[column], bins=20, color='blue', alpha=0.7)
    plt.xlabel(column)

plt.tight_layout()
plt.show()

# Apply Min-Max scaling
scaler = MinMaxScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

# Display dataset statistics after scaling
print("\nDataset Statistics After Scaling:")
print(data_scaled.describe())

# Plot the distributions after scaling
plt.figure(figsize=(12, 8))

for i, column in enumerate(data_scaled.columns):
    plt.subplot(2, 2, i+1)
    plt.title(f"Distribution of '{column}' After Scaling")
    plt.hist(data_scaled[column], bins=20, color='green', alpha=0.7)
    plt.xlabel(column)

plt.tight_layout()
plt.show()
