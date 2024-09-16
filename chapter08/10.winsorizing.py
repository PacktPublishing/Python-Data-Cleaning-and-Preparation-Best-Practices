import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.mstats import winsorize

# Generate student data with missing ages and test scores
data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)

# Fill NaN values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Display the original dataset statistics
print("Original Dataset Statistics:")
print(df.describe())

# Plot the distributions before outlier handling
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' Before Outlier Handling")
plt.hist(df['Age'], bins=10, color='blue', alpha=0.7, label='Original')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' Before Outlier Handling")
plt.hist(df['Test_Score'], bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()

# Identify and handle outliers using winsorizing for 'Age' column
winsorizing_fraction = 0.1
df['Age_Winsorized'] = winsorize(df['Age'], limits=[winsorizing_fraction, winsorizing_fraction])

# Display the dataset after winsorizing
print("\nDataset after Winsorizing:")
print(df)

# Display the dataset statistics after winsorizing
print("\nDataset Statistics after Winsorizing:")
print(df.describe())

# Plot the distributions after winsorizing
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' After Winsorizing")
plt.hist(df['Age_Winsorized'], bins=10, color='blue', alpha=0.7, label='Winsorized')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' After Winsorizing")
plt.hist(df['Test_Score'], bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()
