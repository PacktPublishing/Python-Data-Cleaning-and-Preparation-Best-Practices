import pandas as pd

# Create a sample dataset
data = {
    'ProductID': [1, 2, 3, 4, 5],
    'ProductName': ['PROD001', 'PROD002', 'Product003', 'PROD004', 'PROD005'],
}

df = pd.DataFrame(data)

# Define the expected prefix
expected_prefix = "PROD"

# Check consistency and create a boolean mask for inconsistent names
inconsistent_mask = ~df['ProductName'].str.startswith(expected_prefix)

# Create a new column to indicate consistency
df['Consistency'] = ~inconsistent_mask

# Calculate the percentage of consistent rows
consistent_percentage = (df['Consistency'].sum() / len(df)) * 100

# Display the dataset with the consistency check results
print("Dataset with Consistency Check:")
print(df)

# Display the percentage of consistent rows
print(f"Percentage of Consistent Rows: {consistent_percentage:.2f}%")