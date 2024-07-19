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

# Define window size for SMA and span for EMA
window_size = 20
span = 20

# Calculate Simple Moving Average (SMA)
df['SMA'] = df['close'].rolling(window=window_size, min_periods=1).mean()

# Calculate Exponential Moving Average (EMA)
df['EMA'] = df['close'].ewm(span=span, adjust=False).mean()

# Calculate residuals for SMA and EMA
df['SMA_residuals'] = df['close'] - df['SMA']
df['EMA_residuals'] = df['close'] - df['EMA']

# Performance Metrics Calculation
sma_mae = mean_absolute_error(df['close'], df['SMA'])
sma_mse = mean_squared_error(df['close'], df['SMA'])
sma_rmse = np.sqrt(sma_mse)

ema_mae = mean_absolute_error(df['close'], df['EMA'])
ema_mse = mean_squared_error(df['close'], df['EMA'])
ema_rmse = np.sqrt(ema_mse)

# Plotting original 'close', SMA, and EMA
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['close'], label='Original Close Price', marker='o', linestyle='-', color='b')
plt.plot(df.index, df['SMA'], label=f'Simple Moving Average (window={window_size})', linestyle='--', color='r')
plt.plot(df.index, df['EMA'], label=f'Exponential Moving Average (span={span})', linestyle='-.', color='g')
plt.title('Simple vs. Exponential Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plotting Performance Metrics
metrics = ['MAE', 'MSE', 'RMSE']
sma_values = [sma_mae, sma_mse, sma_rmse]
ema_values = [ema_mae, ema_mse, ema_rmse]

plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(metrics))

plt.bar(index, sma_values, bar_width, label='Simple Moving Average (SMA)', color='b')
plt.bar(index + bar_width, ema_values, bar_width, label='Exponential Moving Average (EMA)', color='g')

plt.xlabel('Metrics')
plt.ylabel('Value')
plt.title('Performance Metrics: SMA vs. EMA')
plt.xticks(index + bar_width / 2, metrics)
plt.legend()
plt.tight_layout()
plt.show()
