import pandas as pd

# Sample employee data
employee_data = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT']
})

# Sample project assignment data
project_data = pd.DataFrame({
    'employee_id': [2, 3, 4, 5, 6],
    'project_name': ['ProjectA', 'ProjectB', 'ProjectC', 'ProjectD', 'ProjectE']
})

# Performing an inner join
merged_data = pd.merge(employee_data, project_data, on='employee_id', how='inner')

# Displaying the results
print("Merged Data Result:")
print(merged_data)