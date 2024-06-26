import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from category_encoders import BinaryEncoder

# Sample data
data = {
    'Country': ['USA', 'Canada', 'USA', 'Canada', 'Mexico', 'USA', 'Mexico', 'Canada'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'Income': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    'Subscription': [1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Plot the distribution of the 'Country' feature before encoding
plt.figure(figsize=(10, 6))
sns.countplot(x='Country', data=df)
plt.title('Distribution of Country Feature Before Encoding')
plt.show()

# Apply binary encoding to the 'Country' feature
encoder = BinaryEncoder(cols=['Country'])
df_encoded = encoder.fit_transform(df)

# Display the encoded dataframe
print(df_encoded)

# Plot the distribution of the binary encoded features
encoded_cols = [col for col in df_encoded.columns if 'Country' in col]
n_cols = len(encoded_cols)

fig, axes = plt.subplots(1, n_cols, figsize=(5*n_cols, 5))
fig.suptitle('Distribution of Country Feature After Binary Encoding')

for i, col in enumerate(encoded_cols):
    sns.histplot(df_encoded[col], kde=True, ax=axes[i], bins=2)
    axes[i].set_title(col)
    axes[i].set_xlabel('Encoded Value')
    axes[i].set_ylabel('Count')

plt.tight_layout()
plt.show()