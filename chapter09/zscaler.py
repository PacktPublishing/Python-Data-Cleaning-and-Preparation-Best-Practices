import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
# Create a DataFrame with all features
data = pd.DataFrame({
    'Square_Footage': square_footage,
    'Distance_to_School': distance_to_school,
    'Commute_Distance': commute_distance,
    'Traffic_Density': traffic_density
})

# Print original dataset statistics
print("Original Dataset Statistics:")
print(data.describe())

# Visualize the original distributions
data.hist(figsize=(12, 10), bins=20, color='blue', alpha=0.7)
plt.suptitle('Original Data Distributions')
plt.show()

# Z-score scaling
data_zscore = (data - data.mean()) / data.std()

# Print dataset statistics after Z-score scaling
print("\nDataset Statistics after Z-score Scaling:")
print(data_zscore.describe())

# Visualize the distributions after Z-score scaling
data_zscore.hist(figsize=(12, 10), bins=20, color='green', alpha=0.7)
plt.suptitle('Data Distributions after Z-score Scaling')
plt.show()
