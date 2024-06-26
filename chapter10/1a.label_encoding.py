import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset 
data = { 
    'Employee Rating': ['Poor', 'Good', 'Satisfactory', 'Excellent', 'Good'], 
    'Salary': [35000, 50000, 42000, 60000, 52000],
    'Years of Experience': [2, 5, 3, 8, 6],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing'] 
} 

df = pd.DataFrame(data) 
print("Original DataFrame:")
print(df)

# Initialize the LabelEncoder 
label_encoder = LabelEncoder() 

# Apply label encoding to the 'Employee Rating' column 
df['Employee Rating (Encoded)'] = label_encoder.fit_transform(df['Employee Rating']) 

print("\nDataFrame after Label Encoding:")
print(df) 

# Plot the distribution of the 'Employee Rating' column before encoding
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.countplot(x='Employee Rating', data=df, order=df['Employee Rating'].value_counts().index)
plt.title('Distribution of Employee Rating (Before Encoding)')
plt.xlabel('Employee Rating')
plt.ylabel('Count')

# Plot the distribution of the 'Employee Rating (Encoded)' column after encoding
plt.subplot(1, 2, 2)
sns.countplot(x='Employee Rating (Encoded)', data=df, order=df['Employee Rating (Encoded)'].value_counts().index)
plt.title('Distribution of Employee Rating (After Encoding)')
plt.xlabel('Employee Rating (Encoded)')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
