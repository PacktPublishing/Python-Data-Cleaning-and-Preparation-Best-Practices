import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate time series data with missing values
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
data_with_missing = pd.Series([1, 2, np.nan, 4, 5, 6, np.nan, 8, 9, 10], index=date_rng)

# Interpolate missing values using linear interpolation
data_interpolated_linear = data_with_missing.interpolate(method='linear')

# Plotting the original and interpolated data
plt.figure(figsize=(10, 5))
plt.plot(data_with_missing, marker='o', label='Original Data', linestyle='--')
plt.plot(data_interpolated_linear, marker='x', label='Interpolated Data', linestyle='-')
plt.title('Original and Interpolated Time Series Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
