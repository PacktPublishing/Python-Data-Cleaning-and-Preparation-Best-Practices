import pandas as pd
import numpy as np
from time import time

# Number of rows for the benchmarking example
num_rows = 5

# Creating two sample DataFrames with identical keys and some identical columns
employee_data_1 = pd.DataFrame({
    'employee_id': np.arange(num_rows),
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT'],
    'salary': [50000, 60000, 70000, 80000, 90000]
})

employee_data_2 = pd.DataFrame({
    'employee_id': np.arange(num_rows),
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Sales', 'Finance', 'Operations'],
    'bonus': [3000, 4000, 5000, 6000, 7000]
})

# Utilizing indexes
employee_data_1.set_index('employee_id', inplace=True)
employee_data_2.set_index('employee_id', inplace=True)

# Sort indexes
employee_data_1.sort_index(inplace=True)
employee_data_2.sort_index(inplace=True)

# Merge operation
start_time = time()
merged_data = pd.merge(employee_data_1, employee_data_2, left_index=True, right_index=True, suffixes=('_1', '_2'))
end_time = time()
merge_time = end_time - start_time

# Displaying the merged DataFrame
print("Merged Employee Data:")
print(merged_data)
print(f"Merge operation took: {merge_time:.5f} seconds")

# Reduce memory usage by downcasting numerical columns
employee_data_1['salary'] = pd.to_numeric(employee_data_1['salary'], downcast='integer')
employee_data_2['bonus'] = pd.to_numeric(employee_data_2['bonus'], downcast='integer')

# Repeating the merge operation after reducing memory usage
start_time = time()
merged_data_reduced = pd.merge(employee_data_1, employee_data_2, left_index=True, right_index=True, suffixes=('_1', '_2'))
end_time = time()
merge_reduced_time = end_time - start_time

print(f"Merge operation after optimisation took: {merge_reduced_time:.5f} seconds")