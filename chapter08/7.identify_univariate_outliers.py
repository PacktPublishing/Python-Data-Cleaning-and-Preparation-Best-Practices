import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Original dataset
data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)

# Calculate Z-Scores for each column
z_scores_age = np.abs(stats.zscore(df['Age'].dropna()))
z_scores_test_score = np.abs(stats.zscore(df['Test_Score'].dropna()))

# Set Z-Score threshold
z_threshold = 3

# Identify outliers
outliers_age = np.where(z_scores_age > z_threshold)[0]
outliers_test_score = np.where(z_scores_test_score > z_threshold)[0]

# Plot Z-Scores
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Z-Scores for 'Age'")
plt.scatter(range(len(z_scores_age)), z_scores_age, color='blue', label='Z-Scores')
plt.axhline(y=z_threshold, color='red', linestyle='--', label='Threshold')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Z-Scores for 'Test_Score'")
plt.scatter(range(len(z_scores_test_score)), z_scores_test_score, color='orange', label='Z-Scores')
plt.axhline(y=z_threshold, color='red', linestyle='--', label='Threshold')
plt.legend()

plt.tight_layout()
plt.show()

# Function to identify outliers using IQR
def identify_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

# Identify and print outliers for 'Age'
age_outliers = identify_outliers('Age')
print("Outliers in 'Age':")
print(age_outliers)

# Identify and print outliers for 'Test_Score'
test_score_outliers = identify_outliers('Test_Score')
print("\nOutliers in 'Test_Score':")
print(test_score_outliers)

# Visualize the distribution of 'Age' and 'Test_Score' using box plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Box Plot of 'Age'")
plt.boxplot(df['Age'].dropna())
plt.xticks([1], ['Age'])

plt.subplot(1, 2, 2)
plt.title("Box Plot of 'Test_Score'")
plt.boxplot(df['Test_Score'].dropna())
plt.xticks([1], ['Test_Score'])

plt.tight_layout()
plt.show()
