import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate example univariate time series data
date_rng = pd.date_range(start='2010-01-01', end='2020-12-31', freq='M')
temperature_data = pd.Series(np.random.normal(20, 5, len(date_rng)), index=date_rng)

# Plotting the univariate time series data
plt.figure(figsize=(10, 5))
plt.plot(temperature_data, label='Temperature Data')
plt.title('Univariate Time Series Data')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()
