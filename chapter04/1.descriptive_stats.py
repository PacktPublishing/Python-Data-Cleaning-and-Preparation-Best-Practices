import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the initial and expanded e-commerce dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'ProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_C'],
    'PurchaseAmount': [50, 75, 120, 60, 80, 55, 90, 110, 70, 85, 130],
    'PaymentMethod': ['Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card'],
    'Timestamp': ['2022-01-01 08:30:45', '2022-01-02 14:20:30', '2022-01-03 20:15:10', '2022-01-04 12:45:30', '2022-01-05 18:10:55', '2022-01-06 09:30:15', '2022-01-07 15:40:20', '2022-01-08 22:25:50', '2022-01-09 14:55:45', '2022-01-10 19:30:10', '2022-01-11 08:45:30']
}

df = pd.DataFrame(data)

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Display the initial and expanded dataset
print("Initial and Expanded Dataset:")
print(df)

# Remove irrelevant column 'CustomerID'
df = df.drop(columns=['CustomerID'])

# Descriptive statistics
desc_stats = df.describe()
print("\nDescriptive Statistics:")
print(desc_stats)

# Visualize distributions
plt.figure(figsize=(15, 8))

# Distribution of Purchase Amount
plt.subplot(2, 2, 1)
sns.histplot(df['PurchaseAmount'], kde=True, color='skyblue')
plt.title('Distribution of Purchase Amount')

# Distribution of Payment Methods
plt.subplot(2, 2, 2)
sns.countplot(x='PaymentMethod', data=df, palette='Set2')
plt.title('Distribution of Payment Methods')

# Distribution of Product Names
plt.subplot(2, 1, 2)
sns.countplot(x='ProductName', data=df, palette='Set2')
plt.title('Distribution of Product Names')

plt.tight_layout()
plt.show()
