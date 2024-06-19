import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Generate synthetic time series data with autocorrelation
np.random.seed(42)
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
autocorr_data = 0.7 * np.sin(np.arange(len(date_rng)) * (2 * np.pi / 30)) + np.random.normal(0, 0.5, size=len(date_rng))
time_series_data = pd.Series(autocorr_data, index=date_rng)

# Visualize the original time series
plt.figure(figsize=(10, 5))
plt.plot(time_series_data, label='Original Data')
plt.title('Synthetic Time Series with Autocorrelation')
plt.legend()
plt.show()

# Perform autocorrelation analysis
plot_acf(time_series_data)
plt.title('Autocorrelation Function (ACF)')
plt.show()
