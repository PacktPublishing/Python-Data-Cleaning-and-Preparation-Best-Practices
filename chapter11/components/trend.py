import pandas as pd
import matplotlib.pyplot as plt

# Generate example data
date_rng = pd.date_range(start='2010-01-01', end='2020-12-31', freq='M')
sales_data = pd.Series(range(1, len(date_rng) + 1), index=date_rng)

# Plotting the time series data with a trend
plt.figure(figsize=(10, 5))
plt.plot(sales_data, label='Sales Data')
plt.title('Time Series Data with Trend')
plt.xlabel('Time')
plt.ylabel('Sales')
plt.legend()
plt.show()
