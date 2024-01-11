import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mstats

# Generate a dataset with extreme values
data_with_outliers = pd.Series([10, 12, 15, 22, 500, 24, 66, 45,  35,500, 400, 40, 38, 30, 22, 15, 12])

# Winsorize the data at the 95th percentile
winsorized_data = mstats.winsorize(data_with_outliers, limits=[0.2, 0.2])

# Plotting the original and winsorized data
plt.figure(figsize=(10, 5))
plt.plot(data_with_outliers, marker='o', label='Original Data', linestyle='--')
plt.plot(winsorized_data, marker='x', label='Winsorized Data', linestyle='-')
plt.title('Original and Winsorized Data')
plt.xlabel('Data Point')
plt.ylabel('Value')
plt.legend()
plt.show()
