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
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S')

# Sort DataFrame by 'Timestamp'
df.sort_values(by='Timestamp', inplace=True)

# Calculate time differences and add to DataFrame
df['TimeSincePreviousPurchase'] = df['Timestamp'].diff()
df['TimeUntilNextPurchase'] = -df['Timestamp'].diff(-1)

# Display the DataFrame with timedelta columns
print("DataFrame with Time Differences:")
print(df[['Timestamp', 'TimeSincePreviousPurchase', 'TimeUntilNextPurchase']])

# Create diff with longer periods
df['TimeDifference2periods'] = df['Timestamp'].diff(periods=2)

print("DataFrame with Time Differences:")
print(df[['Timestamp', 'TimeSincePreviousPurchase', "TimeDifference2periods"]])

# Fill missing values on diff
df['TimeDiff2periods_nonulls'] = df['Timestamp'].diff(periods=2).fillna(0)
print("DataFrame with Time Differences:")
print(df[['Timestamp', 'TimeDiff2periods_nonulls', "TimeDifference2periods"]])

