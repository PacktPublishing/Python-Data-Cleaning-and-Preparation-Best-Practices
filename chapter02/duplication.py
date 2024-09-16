import pandas as pd

# Create a sample dataset with duplicate records
data = {
    'EmployeeID': [101, 102, 103, 101, 104, 105, 102],
    'FirstName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Bob'],
    'LastName': ['Smith', 'Johnson', 'Brown', 'Davis', 'Lee', 'White', 'Johnson'],
}

df = pd.DataFrame(data)

# Check for duplicate records based on the 'EmployeeID' column
duplicated_mask = df.duplicated(subset='EmployeeID', keep='first')

# Create a new column to indicate duplicate records
df['IsDuplicate'] = duplicated_mask

# Calculate the percentage of duplicate records
duplicate_percentage = (df['IsDuplicate'].sum() / len(df)) * 100

# Display the dataset with the duplicate records marked
print("Dataset with Duplicate Records:")
print(df)

# Display the percentage of duplicate records
print(f"Percentage of Duplicate Records: {duplicate_percentage:.2f}%")
