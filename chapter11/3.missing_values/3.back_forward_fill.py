import pandas as pd
import numpy as np

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

# Fill NaN values using forward fill and backward fill
df['close_ffill'] = df['close'].ffill()  # Forward Fill
df['close_bfill'] = df['close'].bfill()  # Backward Fill

# Display the entire DataFrame including original and filled values
print("Complete DataFrame with Original and Filled Values:\n")
print(df[['open', 'close', 'close_ffill', 'close_bfill']].head(20))  # Show first 20 rows
