import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample dataset with missing values
np.random.seed(42)

data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)

# Create indicator variables for missing values
df['Age_missing'] = df['Age'].isnull().astype(int)
df['Test_Score_missing'] = df['Test_Score'].isnull().astype(int)

# Display the original dataset
print("Original Dataset:")
print(df)

# Impute missing values with a placeholder (e.g., mean or median)
df_imputed = df.copy()
df_imputed['Age'].fillna(df_imputed['Age'].mean(), inplace=True)
df_imputed['Test_Score'].fillna(df_imputed['Test_Score'].mean(), inplace=True)

# Display the dataset after imputation
print("\nDataset after Indicator Variable Imputation:")
print(df_imputed)

# Plot distribution charts for indicator variables
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of Age_missing")
df['Age_missing'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.xlabel("Missing (1) / Not Missing (0)")
plt.ylabel("Count")

plt.subplot(1, 2, 2)
plt.title("Distribution of Test_Score_missing")
df['Test_Score_missing'].value_counts().plot(kind='bar', color=['blue', 'orange'])
plt.xlabel("Missing (1) / Not Missing (0)")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

import seaborn as sns

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(x='Age_missing', y='Test_Score', data=df_imputed)
plt.title("Boxplot of Test_Score by Age_missing")

plt.subplot(1, 2, 2)
sns.boxplot(x='Test_Score_missing', y='Age', data=df_imputed)
plt.title("Boxplot of Age by Test_Score_missing")

plt.tight_layout()
plt.show()

