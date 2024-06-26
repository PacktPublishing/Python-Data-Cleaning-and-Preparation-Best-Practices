import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from category_encoders import CountEncoder  # Ensure you have this library installed

# Create a sample dataset
data = {
    'Customer ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Books', 'Clothing', 'Electronics', 'Books', 'Clothing', 'Books'],
    'Total Purchases': [5, 2, 3, 8, 7, 4, 2, 5, 1, 6]
}

df = pd.DataFrame(data)

# Display the sample dataset
print("Sample Dataset:")
print(df)

# Define the features
X = df[['Customer ID', 'Product Category', 'Total Purchases']]

# Split the data into training and testing sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Initialize the CountEncoder for 'Product Category'
count_encoder = CountEncoder(cols=['Product Category'])

# Fit and transform the training data
X_train_encoded = count_encoder.fit_transform(X_train)

# Transform the test data using the same encoder
X_test_encoded = count_encoder.transform(X_test)

# Plot the distribution of the original and encoded 'Product Category' in the training set
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Original 'Product Category' distribution
sns.countplot(ax=axes[0], x='Product Category', data=X_train).set_title('Original Product Category Distribution (Training Set)')

# Encoded 'Product Category' distribution
sns.countplot(ax=axes[1], x='Product Category', data=X_train_encoded).set_title('Encoded Product Category Distribution (Training Set)')

plt.tight_layout()
plt.show()

# Display the encoded training dataset
print("\nEncoded Training Dataset:")
print(X_train_encoded.head())

# Display the encoded testing dataset
print("\nEncoded Testing Dataset:")
print(X_test_encoded.head())
