import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate student data with missing ages and test scores
data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38 ],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59]}

df = pd.DataFrame(data)

# Detect missing values
missing_values = df.isnull()


# Check if there are any missing values in the entire DataFrame
any_missing = missing_values.any().any()

print("Are there any missing values in the dataset?", any_missing)
print("\nMissing Values Detection:")
print(missing_values)

# Count the number of null rows
null_rows_count = df.isnull().any(axis=1).sum()

print("Count of Rows with at least one Missing Value:", null_rows_count)
print(8/len(df))