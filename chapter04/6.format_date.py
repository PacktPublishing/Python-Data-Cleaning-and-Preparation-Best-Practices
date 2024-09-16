import pandas as pd

# Sample dataset
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'ProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_C'],
    'PurchaseAmount': [50, 75, 120, 60, 80, 55, 90, 110, 70, 85, 130],
    'PaymentMethod': ['Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card'],
    'Timestamp': ['2022-01-01 08:30:45', '2022-01-02 14:20:30', '2022-01-03 20:15:10', '2022-01-04 12:45:30', '2022-01-05 18:10:55', '2022-01-06 09:30:15', '2022-01-07 15:40:20', '2022-01-08 22:25:50', '2022-01-09 14:55:45', '2022-01-10 19:30:10', '2022-01-11 08:45:30']
}

df = pd.DataFrame(data)
print(df)

# Ensure 'Timestamp' column is of type datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S')

# Display the DataFrame after parsing
print("\nDataFrame After Parsing:")
print(df)

# Method 4: Using strftime for custom formatting
# Comment: The strftime method is used to customize the display format of datetime objects
df['FormattedTimestamp'] = df['Timestamp'].dt.strftime('%b %d, %Y %I:%M %p')

# Display the DataFrame with the formatted timestamp
print("\nDataFrame with Formatted Timestamp:")
print(df[['Timestamp', 'FormattedTimestamp']])

# Display data types of columns
print("\nData Types of Columns After Transformations:")
print(df.dtypes)
