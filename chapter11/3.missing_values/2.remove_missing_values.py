import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate date range and random stock prices
date_range = pd.date_range(start='2020-01-01', end='2023-12-31', freq='B')
n = len(date_range)
data = {
    'open': np.random.uniform(100, 200, n),
    'high': np.random.uniform(200, 300, n),
    'low': np.random.uniform(50, 100, n),
    'close': np.random.uniform(100, 200, n)
}
df = pd.DataFrame(data, index=date_range)

# Introduce random NaN values in 'close' and 'open' columns
nan_indices_close = np.random.choice(df.index, size=50, replace=False)
nan_indices_open = np.random.choice(df.index, size=50, replace=False)
df.loc[nan_indices_close, 'close'] = np.nan
df.loc[nan_indices_open, 'open'] = np.nan

# Display the first few rows of the DataFrame
print("Initial DataFrame with Missing Values:\n", df.head())

# Step 1: Checking for NaNs or Null Values in columns
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:\n", missing_values)

# Print percentage of missing values in each column
missing_percentage = (missing_values / len(df)) * 100
print("\nPercentage of Missing Values in Each Column:\n", missing_percentage)

# Print the number of rows before dropping NaN values
print(f"\nNumber of rows before dropping NaN values: {len(df)}")

# Step 2: Drop rows with NaN values
df_cleaned = df.dropna()

# Print the number of rows after dropping NaN values
print(f"\nNumber of rows after dropping NaN values: {len(df_cleaned)}")

# Print percentage of missing values after dropping NaN values
cleaned_missing_values = df_cleaned.isnull().sum()
cleaned_missing_percentage = (cleaned_missing_values / len(df_cleaned)) * 100
print("\nPercentage of Missing Values After Dropping Rows:\n", cleaned_missing_percentage)

# Plotting original data with NaN values
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['close'], marker='o', linestyle='-', label='Original Closing Price', color='blue', alpha=0.5)

# Highlight points with NaN values in the original dataset
nan_dates_close = df.index[df['close'].isnull()]
nan_dates_open = df.index[df['open'].isnull()]

# Use 'x' marker for the points to be dropped
plt.scatter(nan_dates_close, [df['close'].mean()] * len(nan_dates_close), color='orange', label='NaN Values in Close (To be Dropped)', marker='x', zorder=5)
plt.scatter(nan_dates_open, [df['close'].mean()] * len(nan_dates_open), color='red', label='NaN Values in Open (To be Dropped)', marker='x', zorder=5)

plt.title('Original Daily Closing Prices with NaN Values Highlighted')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

# Plotting cleaned data after dropping rows with NaN values
plt.figure(figsize=(14, 7))
plt.plot(df_cleaned.index, df_cleaned['close'], marker='o', linestyle='-', label='Cleaned Closing Price', color='green')

plt.title('Cleaned Daily Closing Prices After Dropping NaN Values')
plt
