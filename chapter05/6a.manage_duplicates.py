import pandas as pd

# Sample employee data with potential duplicate keys
employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva', 'Eva'],
    'department': ['HR', 'IT', 'IT', 'Marketing', 'Finance', 'IT', 'IT']
})

# Sample project assignment data with potential duplicate keys
project_data = pd.DataFrame({
    'employee_id': [2, 3, 4, 5, 5, 6],
    'project_name': ['ProjectA', 'ProjectB', 'ProjectC', 'ProjectD', 'ProjectD', 'ProjectE']
})

# Handling duplicates
## Drop duplicates
employee_data = employee_data.drop_duplicates(subset='employee_id', keep='first')
project_data = project_data.drop_duplicates(subset='employee_id', keep='first')

# Performing a merge
merged_data = pd.merge(employee_data, project_data, on='employee_id', how='inner')

# Displaying the results
print("Merged Data Result after handling duplicates:")
print(merged_data)