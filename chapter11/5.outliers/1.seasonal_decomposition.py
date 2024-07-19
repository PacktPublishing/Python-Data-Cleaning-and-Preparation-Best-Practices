import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
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

# Decompose the series
result = seasonal_decompose(df['close'], model='additive', period=252, extrapolate_trend='freq')

# Add decomposed components to DataFrame
df['trend'] = result.trend
df['seasonal'] = result.seasonal
df['residual'] = result.resid

# Calculate Z-scores of residuals to identify outliers
df['resid_z'] = zscore(df['residual'].dropna())

# Identify outliers (Z-score threshold set to 3)
outliers = df[np.abs(df['resid_z']) > 3]

# Handling outliers by replacing them with the median of the residuals
median_resid = df['residual'].median()
df.loc[outliers.index, 'close'] = df['close'].median()

# Print the DataFrame to understand the numbers
print(df[['close', 'close', 'trend', 'seasonal', 'residual', 'resid_z']].head(20))

# Plot the decomposed components
fig, axes = plt.subplots(4, 1, figsize=(14, 18), sharex=True)

result.observed.plot(ax=axes[0], title='Observed', color='blue')
result.trend.plot(ax=axes[1], title='Trend', color='orange')
result.seasonal.plot(ax=axes[2], title='Seasonal', color='green')
result.resid.plot(ax=axes[3], title='Residual', color='red')

plt.tight_layout()
plt.show()
