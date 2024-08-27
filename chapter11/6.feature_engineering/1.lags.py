import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

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

# Introduce more aggressive outliers in the 'close' column
outlier_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[outlier_indices[:5], 'close'] = df['close'] * 1.5  # Increase by 50%
df.loc[outlier_indices[5:], 'close'] = df['close'] * 0.5  # Decrease by 50%

# Function to create lagged features
def create_lagged_features(df, column, lags):
    for lag in lags:
        df[f'{column}_lag_{lag}'] = df[column].shift(lag)
    return df

# Define the lags to create
lags = [5, 10, 20]

# Create lagged features for 'close' column
df = create_lagged_features(df, 'close', lags)

# Plotting original 'close' and lagged features in separate subplots
plt.figure(figsize=(14, 10))

# First subplot for the original 'close' price
plt.subplot(len(lags) + 1, 1, 1)
plt.plot(df.index, df['close'], label='Original Close Price', linestyle='-', color='b')
plt.title('Original Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Create additional subplots for each lagged feature
for i, lag in enumerate(lags):
    plt.subplot(len(lags) + 1, 1, i + 2)
    plt.plot(df.index, df[f'close_lag_{lag}'], label=f'Lag {lag}', linestyle='-', color='b')
    plt.title(f'Lag {lag} Feature')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()

plt.tight_layout()  # Adjust spacing between plots
plt.show()

# Explanation of significance of lagged features
print("Explanation of Lagged Features:")
print("- Lagged features, such as Lag 1, Lag 5, Lag 10, and Lag 20, represent historical values of the 'close' price.")
print("- They capture temporal dependencies and autocorrelation present in the data.")
print("- Lagged features are important for predicting future movements based on past behavior.")
print("- They help in identifying trends, cycles, and seasonality in time series data.")
