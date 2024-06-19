import pandas as pd

# Create a sample dataset
data = {
    'Email': ['john.doe@example.com', 'jane.smith@example.com', 'james.doe@example.com', 'susan.brown@example.com'],
}

df = pd.DataFrame(data)

# Check uniqueness and create a boolean mask for duplicated email addresses
duplicated_mask = df['Email'].duplicated(keep='first')

# Create a new column to indicate uniqueness
df['Uniqueness'] = ~duplicated_mask

# Calculate the percentage of unique records
unique_percentage = (df['Uniqueness'].sum() / len(df)) * 100

# Display the dataset with the uniqueness check results
print("Dataset with Uniqueness Check:")
print(df)

# Display the percentage of unique records
print(f"Percentage of Unique Records: {unique_percentage:.2f}%")
