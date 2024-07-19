import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from scipy.stats import zscore

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


# Fit ARIMA model to close_filled series
model = ARIMA(df['close'], order=(2, 1, 1)) 
results = model.fit()

# Calculate residuals and Z-scores
df['residuals'] = results.resid
df['residuals_z'] = zscore(df['residuals'].dropna())

# Identify outliers based on Z-score threshold (e.g., ±3)
outliers_arima = df[np.abs(df['residuals_z']) > 3]

# Generate smoothed series from ARIMA model
df['arima_smooth'] = results.fittedvalues

# Plotting the original close_filled and ARIMA smoothed series
plt.figure(figsize=(14, 8))
plt.plot(df['close'], label='Original Close', color='blue')
plt.plot(df['arima_smooth'], label='ARIMA Smoothed', color='red')
plt.scatter(outliers_arima.index, df.loc[outliers_arima.index, 'close'], color='orange', label='Outliers')
plt.title('ARIMA Smoothing and Outlier Detection')
plt.legend()
plt.show()

# Print the summary of the model
print(results.summary())

# Plot the diagnostics to check model fit
results.plot_diagnostics(figsize=(14, 8))
plt.show()
