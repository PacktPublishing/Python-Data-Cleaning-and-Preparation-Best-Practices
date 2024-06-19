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

# Performing a merge with validation to ensure no duplicates in the key column of the left DataFrame
try:
    merged_data = pd.merge(employee_data, project_data, on='employee_id', how='inner', validate='one_to_many')
    print("Merged Data Result:")
    print(merged_data)
except ValueError as e:
    print("Merge failed:", e)
    