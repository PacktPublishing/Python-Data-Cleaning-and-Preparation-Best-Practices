import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Generate time series data with missing values
date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')
data_with_missing = pd.Series([1, 2, np.nan, 4, 5, 6, np.nan, 8, 9, 10], index=date_rng)

# Create a function for polynomial interpolation
poly_interpolator = interp1d(data_with_missing.dropna().index.values.astype(float),
                             data_with_missing.dropna().values,
                             kind='polynomial',
                             fill_value='extrapolate')

# Interpolate missing values using polynomial interpolation
data_interpolated_poly = poly_interpolator(data_with_missing.index.values.astype(float))

# Plotting the original and polynomial interpolated data
plt.figure(figsize=(10, 5))
plt.plot(data_with_missing, marker='o', label='Original Data', linestyle='--')
plt.plot(data_interpolated_poly, marker='x', label='Polynomial Interpolation', linestyle='-')
plt.title('Original and Polynomial Interpolated Time Series Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
