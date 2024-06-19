import pandas as pd

# Creating a sample DataFrame with potential duplicate keys
employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Marketing', 'Finance', 'IT', 'HR']
})

# Displaying the original DataFrame
print("Original Employee Data:")
print(employee_data)

# Concatenating department names for each employee_id
employee_data['department'] = employee_data.groupby('employee_id')['department'].transform(lambda x: ', '.join(x))
# Removing duplicate entries based on employee_id
employee_data = employee_data.drop_duplicates('employee_id')

# Displaying the modified DataFrame
print("\nModified Employee Data after Concatenation and Removing Duplicates:")
print(employee_data)