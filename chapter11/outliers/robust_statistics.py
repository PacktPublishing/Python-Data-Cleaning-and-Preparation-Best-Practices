
import pandas as pd
import matplotlib.pyplot as plt

# Generate a sample dataset with exam scores (including outliers)
exam_scores = pd.Series([75, 82, 88, 90, 95, 100, 120, 78, 85, 92])

# Calculate mean and median
mean_score = exam_scores.mean()
median_score = exam_scores.median()

# Display descriptive statistics
descriptive_stats = exam_scores.describe()

# Plotting mean vs median
plt.figure(figsize=(8, 6))

# Original Data Histogram
plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black', alpha=0.7, label='Exam Scores')
plt.axvline(x=mean_score, color='orange', linestyle='--', label='Mean')
plt.axvline(x=median_score, color='green', linestyle='--', label='Median')

plt.title('Mean vs Median of Exam Scores')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.legend()

plt.show()

# Display descriptive statistics, mean, and median values
print("Descriptive Statistics:")
print(descriptive_stats)
print("\nMean Exam Score:", mean_score)
print("Median Exam Score:", median_score)
