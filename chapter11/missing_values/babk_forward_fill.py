import pandas as pd
import numpy as np

# Generate time series data with missing values
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
data_with_missing = pd.Series([1, 2, np.nan, 4, 5, 6, np.nan, 8, 9, 10], index=date_rng)

# Display the original data
print("Original Data:")
print(data_with_missing)

# Forward fill missing values
data_forward_filled = data_with_missing.ffill()

# Backward fill missing values
data_backward_filled = data_with_missing.bfill()

# Display the data after forward fill and backward fill
print("\nData after Forward Fill:")
print(data_forward_filled)

print("\nData after Backward Fill:")
print(data_backward_filled)
