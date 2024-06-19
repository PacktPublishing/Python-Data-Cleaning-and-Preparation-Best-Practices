import pandas as pd

# Sample employee data with potential duplicate keys
employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva', 'Eva'],
    'department': ['HR', 'IT', 'IT', 'Marketing', 'Finance', 'IT', 'IT'],
    'salary': [50000, 60000, 60000, 55000, 65000, 70000, 70000]  # Added salary for aggregation
})

# Sample project assignment data with potential duplicate keys
project_data = pd.DataFrame({
    'employee_id': [2, 3, 4, 5, 5, 6],
    'project_name': ['ProjectA', 'ProjectB', 'ProjectC', 'ProjectD', 'ProjectD', 'ProjectE']
})

# Aggregating duplicate entries in employee_data
aggregated_employee_data = employee_data.groupby('employee_id').agg({
    'name': 'first',  # Keep the first name encountered
    'department': 'first',  # Keep the first department encountered
    'salary': 'sum'  # Sum the salaries in case of duplicates
}).reset_index()

# Performing a merge
merged_data = pd.merge(aggregated_employee_data, project_data, on='employee_id', how='inner')

# Displaying the results
print("Merged Data Result after aggregation:")
print(merged_data)