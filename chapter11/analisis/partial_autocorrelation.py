import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Plot the original time series
plt.figure(figsize=(10, 5))
plt.plot(data, label='Number of Passengers')
plt.title('Airline Passenger Dataset')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.legend()
plt.show()

# Perform autocorrelation analysis and plot ACF
plt.figure(figsize=(10, 5))
plot_acf(data, lags=30)  # lags parameter determines the number of lags to show
plt.title('Autocorrelation Function (ACF) Plot')
plt.show()

# Perform partial autocorrelation analysis and plot PACF
plt.figure(figsize=(10, 5))
plot_pacf(data, lags=30)
plt.title('Partial Autocorrelation Function (PACF) Plot')
plt.show()
