import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Create lag features for lags 1, 2, and 3
data['Lag_1'] = data['Passengers'].shift(1)
data['Lag_2'] = data['Passengers'].shift(2)
data['Lag_3'] = data['Passengers'].shift(3)

# Plot the original time series and lagged datasets
plt.figure(figsize=(12, 6))
plt.plot(data['Passengers'], label='Original Data', color='blue')
plt.plot(data['Lag_1'], label='Lag 1', linestyle='--', color='orange')
plt.plot(data['Lag_2'], label='Lag 2', linestyle='--', color='green')
plt.plot(data['Lag_3'], label='Lag 3', linestyle='--', color='red')

plt.title('Airline Passenger Dataset with Lag Features')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.legend()
plt.show()
