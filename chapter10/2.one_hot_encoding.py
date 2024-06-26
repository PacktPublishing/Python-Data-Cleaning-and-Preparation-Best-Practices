import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

# Sample dataset
data = {
    'Customer ID': [1, 2, 3, 4, 5],
    'Contract Type': ['Month-to-Month', 'One Year', 'Month-to-Month', 'Two Year', 'One Year'],
    'Internet Service': ['DSL', 'Fiber Optic', 'DSL', 'Fiber Optic', 'No Internet Service'],
    'Payment Method': ['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card', 'Electronic Check'],
}

df = pd.DataFrame(data)

# Plot distribution of original 'Contract Type' column
plt.figure(figsize=(8, 6))
sns.countplot(x='Contract Type', data=df).set_title('Contract Type Distribution')
plt.show()

# Initialize the OneHotEncoder for 'Contract Type' without dropping any category
one_hot_encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the 'Contract Type' column
encoded_columns = one_hot_encoder.fit_transform(df[['Contract Type']])

# Create a new DataFrame with the one-hot encoded columns for 'Contract Type'
encoded_df = pd.DataFrame(encoded_columns, columns=one_hot_encoder.get_feature_names_out(['Contract Type']))

# Concatenate the one-hot encoded DataFrame with the original DataFrame
df_encoded = pd.concat([df, encoded_df], axis=1)

# Dropping the original 'Contract Type' column as it is now encoded
df_encoded = df_encoded.drop(['Contract Type'], axis=1)

print(df_encoded)

# Plot distribution of encoded 'Contract Type' columns
encoded_cols = encoded_df.columns

fig, axes = plt.subplots(1, len(encoded_cols), figsize=(6 * len(encoded_cols), 5))
for i, col in enumerate(encoded_cols):
    sns.countplot(ax=axes[i], x=encoded_df[col]).set_title(f'{col} Distribution')
plt.tight_layout()
plt.show()
