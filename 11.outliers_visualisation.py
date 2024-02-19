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

# Output identified outliers
print("Outliers in 'Age':", df['Age'].iloc[outliers_age].to_list())
print("Outliers in 'Test_Score':", df['Test_Score'].iloc[outliers_test_score].to_list())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Violin Plot for 'Age'")
plt.violinplot(df['Age'].dropna(), vert=False)

plt.subplot(1, 2, 2)
plt.title("Violin Plot for 'Test_Score'")
plt.violinplot(df['Test_Score'].dropna(), vert=False)

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Box Plot for 'Age'")
plt.boxplot(df['Age'].dropna(), vert=False)

plt.subplot(1, 2, 2)
plt.title("Box Plot for 'Test_Score'")
plt.boxplot(df['Test_Score'].dropna(), vert=False)

plt.tight_layout()
plt.show()
