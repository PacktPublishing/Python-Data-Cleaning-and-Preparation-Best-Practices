import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate example multivariate time series data
date_rng = pd.date_range(start='2010-01-01', end='2020-12-31', freq='M')
temperature_data = pd.Series(np.random.normal(20, 5, len(date_rng)), index=date_rng)
rainfall_data = pd.Series(np.random.normal(50, 20, len(date_rng)), index=date_rng)

# Create a DataFrame with both temperature and rainfall data
multivariate_data = pd.DataFrame({'Temperature': temperature_data, 'Rainfall': rainfall_data})

# Plotting the multivariate time series data
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(multivariate_data['Temperature'], label='Temperature Data', color='blue')
plt.title('Multivariate Time Series Data')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(multivariate_data['Rainfall'], label='Rainfall Data', color='green')
plt.xlabel('Time')
plt.ylabel('Rainfall (mm)')
plt.legend()

plt.tight_layout()
plt.show()
