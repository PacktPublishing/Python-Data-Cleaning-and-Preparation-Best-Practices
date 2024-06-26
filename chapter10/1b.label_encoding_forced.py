import pandas as pd
from sklearn.preprocessing import LabelEncoder

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

# Define the correct order of categories with prefixes
ordered_categories = {
    'Poor': '1.Poor',
    'Satisfactory': '2.Satisfactory',
    'Good': '3.Good',
    'Excellent': '4.Excellent'
}

# Map the 'Employee Rating' column to the prefixed categories
df['Employee Rating Ordered'] = df['Employee Rating'].map(ordered_categories)

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Apply label encoding to the 'Employee Rating Ordered' column
df['Employee Rating (Encoded)'] = label_encoder.fit_transform(df['Employee Rating Ordered'])

# Reverse the mapping for clarity in the DataFrame (optional)
reverse_mapping = {v: k for k, v in ordered_categories.items()}
df['Employee Rating Ordered'] = df['Employee Rating Ordered'].map(reverse_mapping)

print("\nDataFrame after Label Encoding with Correct Order:")
print(df[['Employee Rating Ordered','Employee Rating (Encoded)']])
