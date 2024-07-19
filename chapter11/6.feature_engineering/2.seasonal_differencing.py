import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Set seed for reproducibility
np.random.seed(42)

# Generate date range
date_range = pd.date_range(start='2020-01-01', end='2023-12-31', freq='B')
n = len(date_range)

# Generate a seasonal pattern
seasonal_pattern = np.sin(np.linspace(0, 3 * np.pi, n)) * 20

# Generate random stock prices with added seasonal component
data = {
    'open': np.random.uniform(100, 200, n) + seasonal_pattern,
    'high': np.random.uniform(200, 300, n) + seasonal_pattern,
    'low': np.random.uniform(50, 100, n) + seasonal_pattern,
    'close': np.random.uniform(100, 200, n) + seasonal_pattern
}
df = pd.DataFrame(data, index=date_range)

# Introduce more aggressive outliers in the 'close' column
outlier_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[outlier_indices[:5], 'close'] = df['close'] * 1.5  # Increase by 50%
df.loc[outlier_indices[5:], 'close'] = df['close'] * 0.5  # Decrease by 50%


# First Differencing
df['First Difference'] = df['close'].diff()

# Second Differencing
df['Second Difference'] = df['First Difference'].diff()

# Seasonal Differencing (weekly seasonality)
df['Seasonal Difference'] = df['close'].diff(5)

# Plotting the original series and differenced series
plt.figure(figsize=(14, 10))

plt.subplot(4, 1, 1)
plt.plot(df.index, df['close'], label='Original Series with Seasonality', color='blue')
plt.title('Original Series with Seasonality')
plt.legend(loc='upper right')

plt.subplot(4, 1, 2)
plt.plot(df.index, df['First Difference'], label='First Difference', color='orange')
plt.title('First Differencing')
plt.legend(loc='upper right')

plt.subplot(4, 1, 3)
plt.plot(df.index, df['Second Difference'], label='Second Difference', color='green')
plt.title('Second Differencing')
plt.legend(loc='upper right')

plt.subplot(4, 1, 4)
plt.plot(df.index, df['Seasonal Difference'], label='Seasonal Differencing (Weekly)', color='red')
plt.title('Seasonal Differencing')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Augmented Dickey-Fuller Test
def adf_test(series, title=''):
    result = adfuller(series.dropna(), autolag='AIC')
    print(f'Augmented Dickey-Fuller Test: {title}')
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    for key, value in result[4].items():
        print(f'   {key}: {value}')
    print('\n')

# Perform ADF test on original, first differenced, second differenced, and seasonal differenced series
adf_test(df['close'], title='Original Series')
adf_test(df['close'].diff(), title='First Difference')
adf_test(df['close'].diff().diff(), title='Second Difference')
adf_test(df['Seasonal Difference'], title='Seasonal Differencing')
