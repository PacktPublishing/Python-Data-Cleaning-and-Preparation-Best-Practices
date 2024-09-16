import pandas as pd
import numpy as np

# Creating two sample DataFrames with some identical columns
employee_data_1 = pd.DataFrame({
    'employee_id': np.arange(1, 6),
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT']
})

employee_data_2 = pd.DataFrame({
    'employee_id': np.arange(6, 11),
    'name': ['Frank', 'Grace', 'Hannah', 'Ian', 'Jill'],
    'department': ['Logistics', 'HR', 'IT', 'Marketing', 'Finance']
})

# Concatenating the two DataFrames row-wise
concatenated_data = pd.concat([employee_data_1, employee_data_2], axis=0)

# Displaying the concatenated DataFrame
print("Concatenated Employee Data:")
print(concatenated_data)