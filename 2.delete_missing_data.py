import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate student data with missing ages and test scores
data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59]}

df = pd.DataFrame(data)

# Display the original dataset statistics
print("Original Dataset Statistics:")
print(df.describe())

# Plot the distributions before deletion
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' Before Deletion")
plt.hist(df['Age'].dropna(), bins=10, color='blue', alpha=0.7, label='Original')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' Before Deletion")
plt.hist(df['Test_Score'].dropna(), bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()

# Delete rows with any missing values
df_no_missing = df.dropna()

# Display the dataset after deletion
print("\nDataset after Deleting Rows with Missing Values:")
print(df_no_missing)

# Display the dataset statistics after deletion
print("\nDataset Statistics after Deleting Rows with Missing Values:")
print(df_no_missing.describe())

# Plot the distributions after deletion
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' After Deletion")
plt.hist(df_no_missing['Age'], bins=10, color='blue', alpha=0.7, label='After Deletion')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' After Deletion")
plt.hist(df_no_missing['Test_Score'], bins=10, color='orange', alpha=0.7, label='After Deletion')
plt.legend()

plt.tight_layout()
plt.show()

# Explain the changes and size drop
print("\nExplanation:")
print("The rows containing missing values were removed, resulting in a smaller dataset.")
