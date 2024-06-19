import pandas as pd


# Create the initial and expanded e-commerce dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'ProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_C'],
    'PurchaseAmount': [50, 75, 120, 60, 80, 55, 90, 110, 70, 85, 130],
    'PaymentMethod': ['Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card'],
    'Timestamp': ['2022-01-01 08:30:45', '2022-01-02 14:20:30', '2022-01-03 20:15:10', '2022-01-04 12:45:30', '2022-01-05 18:10:55', '2022-01-06 09:30:15', '2022-01-07 15:40:20', '2022-01-08 22:25:50', '2022-01-09 14:55:45', '2022-01-10 19:30:10', '2022-01-11 08:45:30']
}

df = pd.DataFrame(data)

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Display the initial and expanded dataset
print("Initial and Expanded Dataset:")
print(df)

# Scenario: Renaming Columns with Error Handling

try:
    # Attempt to rename a single column
    df.rename(columns={'ProductName': 'OldProductName'}, inplace=True)
except ValueError as ve:
    print(f"Error: {ve}")

# Check if the column exists before renaming
if 'OldProductName' in df.columns:
    try:
        # Attempt to rename multiple columns
        df.rename(columns={'OldProductName': 'NewProductName', 'PurchaseAmount': 'NewPurchaseAmount'}, inplace=True)
    except ValueError as ve:
        print(f"Error: {ve}")
else:
    print("Error: Column 'OldProductName' does not exist in the DataFrame.")

# Display the dataset after renaming (if successful)
print("\nDataset after Renaming (if successful):")
print(df)
