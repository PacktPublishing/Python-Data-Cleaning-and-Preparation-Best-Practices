import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, None, 28, 22],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City': ['New York', 'Los Angeles', 'Chicago', None, 'San Francisco']
}

df = pd.DataFrame(data)

# Step 1: Import necessary libraries
# We import the pandas library to work with the dataset.

# Step 2: Create a sample dataset
# We create a simple dataset with columns 'Name', 'Age', 'Gender', and 'City'. Some values are intentionally missing (represented as 'None').

# Step 3: Create a DataFrame
df = pd.DataFrame(data)
# We create a DataFrame using the sample data.

# Step 4: Check completeness
completeness = df.isnull().sum()
# The .isnull() method checks for missing values in the DataFrame, and .sum() counts the missing values for each column.

# Step 5: Calculate completeness percentage
total_records = len(df)
completeness_percentage = (1- completeness / total_records) * 100
# We calculate the completeness percentage by dividing the count of missing values by the total number of records and then multiplying by 100.

# Step 6: Display the completeness results
print("Completeness Check:")
print(completeness)
print("\nCompleteness Percentage:")
print(completeness_percentage)
