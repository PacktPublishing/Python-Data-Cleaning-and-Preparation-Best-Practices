import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Calculate Simple Moving Average (SMA) with a window of 12 months
sma_window = 12
data['SMA'] = data['Passengers'].rolling(window=sma_window).mean()

# Plot the original time series and SMA
plt.figure(figsize=(12, 6))
plt.plot(data['Passengers'], label='Original Data')
plt.plot(data['SMA'], label=f'SMA ({sma_window}-Month)', linestyle='--', color='red')
plt.title('Airline Passenger Dataset with Simple Moving Average')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.legend()
plt.show()
