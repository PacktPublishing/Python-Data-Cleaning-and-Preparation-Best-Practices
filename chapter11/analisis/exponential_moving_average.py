import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Calculate Simple Moving Average (SMA) with a window of 12 months
sma_window = 12
data['SMA'] = data['Passengers'].rolling(window=sma_window).mean()

# Calculate Exponential Moving Average (EMA) with a smoothing factor of 0.2
ema_smoothing_factor = 0.2
data['EMA'] = data['Passengers'].ewm(span=sma_window, adjust=False).mean()

# Plot the original time series, SMA, and EMA
plt.figure(figsize=(12, 6))
plt.plot(data['Passengers'], label='Original Data')
plt.plot(data['SMA'], label=f'SMA ({sma_window}-Month)', linestyle='--', color='red')
plt.plot(data['EMA'], label=f'EMA (α={ema_smoothing_factor})', linestyle='--', color='green')
plt.title('Airline Passenger Dataset with SMA and EMA')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.legend()
plt.show()
