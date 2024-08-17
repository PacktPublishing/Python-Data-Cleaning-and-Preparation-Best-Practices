import pandas as pd

# Create the initial e-commerce dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'NewProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_C'],
    'NewPurchaseAmount': [50, 75, 120, 60, 80, 55, 90, 110, 70, 85, 130],
    'PaymentMethod': ['Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card'],
    'Timestamp': ['2022-01-01 08:30:45', '2022-01-02 14:20:30', '2022-01-03 20:15:10', '2022-01-04 12:45:30', '2022-01-05 18:10:55', '2022-01-06 09:30:15', '2022-01-07 15:40:20', '2022-01-08 22:25:50', '2022-01-09 14:55:45', '2022-01-10 19:30:10', '2022-01-11 08:45:30']
}

df = pd.DataFrame(data)

# Display the initial e-commerce dataset
print("Initial E-commerce Dataset:")
print(df)

# Display the initial memory usage
print("Initial Memory Usage:")
print(df.memory_usage().sum() / (1024 ** 2), "MB")  # Convert bytes to megabytes

# Save a copy of the DataFrame before dropping columns for comparison
df_before_drop = df.copy()

# Scenario: Dropping Irrelevant Columns
columns_to_drop = ['CustomerID', 'Timestamp']  # Replace with the names of the columns you want to drop

try:
    # Drop columns considered irrelevant for the current analysis
    df.drop(columns=columns_to_drop, inplace=True)
except KeyError as ke:
    print(f"Error: {ke}")

# Display the DataFrame after dropping columns
print("\nDataFrame after Dropping Irrelevant Columns:")
print(df.columns)

# Display the DataFrame before dropping columns for comparison
print("\nDataFrame Before Dropping Columns:")
print(df_before_drop.columns)

# Display the memory usage after dropping columns
print("\nMemory Usage After Dropping Columns:")
print(df.memory_usage().sum() / (1024 ** 2), "MB")  # Convert bytes to megabytes

