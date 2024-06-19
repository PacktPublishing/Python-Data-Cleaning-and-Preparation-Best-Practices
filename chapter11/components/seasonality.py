import pandas as pd
import matplotlib.pyplot as plt

# Generate example data with seasonality
date_rng = pd.date_range(start='2010-01-01', end='2020-12-31', freq='M')
seasonal_data = pd.Series([10, 12, 15, 22, 30, 35, 40, 38, 30, 22, 15, 12] * 11, index=date_rng)

# Plotting the time series data with seasonality
plt.figure(figsize=(10, 5))
plt.plot(seasonal_data, label='Ice Cream Sales')
plt.title('Time Series Data with Seasonality')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
plt.show()
