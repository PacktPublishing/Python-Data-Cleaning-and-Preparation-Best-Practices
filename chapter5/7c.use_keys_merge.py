import pandas as pd

# Creating two sample DataFrames with identical keys and some identical columns
employee_data_1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT'],
    'salary': [50000, 60000, 70000, 80000, 90000]
})

employee_data_2 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],  # Identical keys
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],  # Identical column
    'department': ['HR', 'IT', 'Sales', 'Finance', 'Operations'],
    'bonus': [3000, 4000, 5000, 6000, 7000]
})

# Merging the two DataFrames with suffixes to differentiate identical columns
merged_data = pd.merge(employee_data_1, employee_data_2, on=['employee_id', 'name'], how='inner', suffixes=('_1', '_2'))

# Displaying the merged DataFrame
print("Merged Employee Data with Identical Keys and Columns:")
print(merged_data)