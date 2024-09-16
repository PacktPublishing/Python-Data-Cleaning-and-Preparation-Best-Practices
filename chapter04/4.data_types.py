import pandas as pd

# Create the initial e-commerce dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'ProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_C'],
    'PurchaseAmount': [50, 75, 120, 60, 80, 55, 90, 110, 70, 85, 130],
    'PaymentMethod': ['Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card'],
    'Timestamp': ['2022-01-01 08:30:45', '2022-01-02 14:20:30', '2022-01-03 20:15:10', '2022-01-04 12:45:30', '2022-01-05 18:10:55', '2022-01-06 09:30:15', '2022-01-07 15:40:20', '2022-01-08 22:25:50', '2022-01-09 14:55:45', '2022-01-10 19:30:10', '2022-01-11 08:45:30']
}

df = pd.DataFrame(data)

# Display the initial e-commerce dataset
print("Initial E-commerce Dataset:")
print(df)

# Inspect data types of columns
print("\nData Types of Columns:")
print(df.dtypes)

# Convert 'PurchaseAmount' to numeric
df['PurchaseAmount'] = pd.to_numeric(df['PurchaseAmount'], errors='coerce')

# Convert 'ProductName' to string
df['ProductName'] = df['ProductName'].astype('str')

# Convert 'PaymentMethod' to categorical
df['PaymentMethod'] = df['PaymentMethod'].astype('category')

# Convert 'CustomerID' to numeric
df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce')

# Add a new boolean column 'HasDevice'
df['HasDive'] = df['ProductName'].str.contains('Dive', case=False)
df['HasDive'] = df['HasDive'].astype('bool')

# Display the dataset after type transformations and adding 'HasDive'
print("\nE-commerce Dataset After Type Transformations and Adding 'HasDive':")
print(df)

# Inspect data types of columns after transformations
print("\nData Types of Columns After Transformations:")
print(df.dtypes)
