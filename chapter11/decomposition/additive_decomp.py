import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate synthetic daily sales data
np.random.seed(42)
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
daily_sales_data = 1000 + 10 * np.sin(np.arange(len(date_rng)) * (2 * np.pi / 365)) + np.random.normal(0, 50, size=len(date_rng))
sales_data = pd.Series(daily_sales_data, index=date_rng)

# Visualize the original time series
plt.figure(figsize=(10, 5))
plt.plot(sales_data, label='Original Data')
plt.title('Original Daily Sales Data')
plt.legend()
plt.show()

# Perform additive decomposition
result_additive = seasonal_decompose(sales_data, model='additive', period=365)

# Visualize additive components
result_additive.plot()
plt.suptitle('Additive Decomposition - Daily Sales Data')
plt.show()
