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

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Localize timestamps to a specific time zone (e.g., 'UTC')
df['Timestamp_UTC'] = df['Timestamp'].dt.tz_localize('UTC')

# Convert localized timestamps to a different time zone (e.g., 'America/New_York')
df['Timestamp_NY'] = df['Timestamp_UTC'].dt.tz_convert('America/New_York')

# Display the DataFrame with time zone-handled timestamps
print(df[['Timestamp', 'Timestamp_UTC', 'Timestamp_NY']])

