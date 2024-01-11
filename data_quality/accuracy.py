import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 28, 28, 22],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'San Francisco']
}

# Reference dataset for accuracy comparison
reference_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 29, 28, 22],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'San Francisco']
}

df = pd.DataFrame(data)
reference_df = pd.DataFrame(reference_data)

# Step 1: Import necessary libraries
# We import the pandas library to work with the dataset.

# Step 2: Create a sample dataset and a reference dataset
# We create a sample dataset and a reference dataset with the same structure.

# Step 3: Create DataFrames
df = pd.DataFrame(data)
reference_df = pd.DataFrame(reference_data)

# Step 4: Compare data to the reference
accuracy_check = df == reference_df

# Step 5: Calculate accuracy percentage
accuracy_percentage = accuracy_check.mean() * 100
# We calculate the accuracy percentage by taking the mean of the accuracy check for each column and multiplying by 100.

# Step 6: Display the accuracy results
print("Accuracy Check:")
print(accuracy_check)
print("\nAccuracy Percentage:")
print(accuracy_percentage)
