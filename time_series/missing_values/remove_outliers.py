import pandas as pd
import numpy as np

# Generate time series data with missing values
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
data_with_missing = pd.Series([1, 2, np.nan, 4, 5, 6, np.nan, 8, 9, 10], index=date_rng)

# Display the original data
print("Original Data:")
print(data_with_missing)

# Remove rows with missing values
data_removed_missing = data_with_missing.dropna()

# Display the data after removing missing values
print("\nData after Removing Missing Values:")
print(data_removed_missing)
