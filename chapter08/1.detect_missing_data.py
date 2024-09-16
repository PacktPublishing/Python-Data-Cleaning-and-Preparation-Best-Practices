import pandas as pd


# Generate student data with missing ages and test scores
data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)
print(df.head())
# Detect missing values
missing_values = df.isnull()

# Check if there are any missing values in the entire DataFrame
any_missing = missing_values.any().any()

print("Are there any missing values in the dataset?", any_missing)
print("\nMissing Values Detection:")
print(missing_values)

# Count the number of null rows
null_rows_count = missing_values.any(axis=1).sum()

print("Count of Rows with at least one Missing Value:", null_rows_count)
print(8/len(df))