import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate example data with noise
date_rng = pd.date_range(start='2010-01-01', end='2020-12-31', freq='M')
np.random.seed(42)
noise_data = pd.Series(np.random.normal(0, 2, len(date_rng)), index=date_rng)

# Plotting the time series data with noise
plt.figure(figsize=(10, 5))
plt.plot(noise_data, label='Temperature Fluctuations')
plt.title('Time Series Data with Noise')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()
