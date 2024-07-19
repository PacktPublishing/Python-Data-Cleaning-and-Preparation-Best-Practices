import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Generate a date range
date_range = pd.date_range(start='2020-01-01', end='2023-12-31', freq='B')  # Business days

# Generate random stock prices
n = len(date_range)
data = {
    'open': np.random.uniform(100, 200, n),
    'high': np.random.uniform(200, 300, n),
    'low': np.random.uniform(50, 100, n),
    'close': np.random.uniform(100, 200, n)
}

# Create DataFrame
df = pd.DataFrame(data, index=date_range)

# Introduce random NaN values
nan_indices = np.random.choice(df.index, size=100, replace=False)
df.loc[nan_indices] = np.nan

# Drop random dates to simulate missing timestamps
missing_dates = np.random.choice(df.index, size=50, replace=False)
df = df.drop(missing_dates)

# Display the first few rows of the DataFrame
print("Initial DataFrame with Missing Values and Timestamps:\n", df.head())

# Step 1: Checking for NaNs or Null Values in columns
missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:\n", missing_values)

# Step 2: Identifying Missing Timestamps
complete_index = pd.date_range(start=df.index.min(), end=df.index.max(), freq='B')  # 'B' is for business days
df_reindexed = df.reindex(complete_index)
missing_timestamps = df_reindexed[df_reindexed.isnull().all(axis=1)]

# Calculate percentage of missing timestamps
total_timestamps = len(complete_index)
missing_timestamps_count = missing_timestamps.shape[0]
missing_timestamps_percentage = (missing_timestamps_count / total_timestamps) * 100

print("\nMissing Timestamps:\n", missing_timestamps)
print(f"\nPercentage of Missing Timestamps: {missing_timestamps_percentage:.2f}%")

# Plotting
plt.figure(figsize=(14, 7))

# Plot the closing prices
plt.plot(df.index, df['close'], marker='o', linestyle='-', label='Closing Price', color='blue')

# Mark missing timestamps with vertical lines
for date in missing_dates:
    plt.axvline(x=date, color='red', linestyle='--', linewidth=1)

# Highlight points with NaN values
nan_dates = df.index[df['close'].isnull()]
plt.scatter(nan_dates, [df['close'].mean()] * len(nan_dates), color='orange', label='NaN Values in Close', zorder=5)

plt.title('Daily Closing Prices with Missing Timestamps and NaN Values Highlighted')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

# Summary of Identifying Missing Values
print("\nNaN values were introduced randomly in the dataset and are highlighted in orange on the plot.\n"
      "Red dashed lines indicate missing timestamps where no data is available for the dates in the index.\n"
      "Blue line shows the closing prices with missing values removed.")

