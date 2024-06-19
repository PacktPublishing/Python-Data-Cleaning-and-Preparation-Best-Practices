import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Compute first-order differences
data['Differences'] = data['Passengers'].diff()

# Compute second-order differences
data['Second_Order_Differences'] = data['Passengers'].diff().diff()

# Plot the original time series and the second-order differenced time series
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(data['Passengers'], label='Original Data', color='blue')
plt.title('Original Time Series')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(data['Differences'], label='First-Order Differences', color='orange')
plt.title('First-Order Differenced Time Series')
plt.xlabel('Month')
plt.ylabel('Differences')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(data['Second_Order_Differences'], label='Second-Order Differences', color='green')
plt.title('Second-Order Differenced Time Series')
plt.xlabel('Month')
plt.ylabel('Second-Order Differences')
plt.legend()

plt.tight_layout()
plt.show()

print(data.head())
