import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Assuming df is your DataFrame with a 'Month' column
df['First_Order_Difference'] = df['Passengers'] - df['Passengers'].shift(1)
df['Second_Order_Difference'] = df['First_Order_Difference'] - df['First_Order_Difference'].shift(1)
df['Seasonal_Difference'] = df['Passengers'] - df['Passengers'].shift(12)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(df['Passengers'], label='Original Data')
plt.title('Original Data')
plt.xlabel('Month')
plt.ylabel('Passengers')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(df['First_Order_Difference'], label='First-Order Differencing')
plt.title('First-Order Differencing')
plt.xlabel('Month')
plt.ylabel('Difference')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot( df['Second_Order_Difference'], label='Second-Order Differencing')
plt.title('Second-Order Differencing')
plt.xlabel('Month')
plt.ylabel('Difference')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(df['Seasonal_Difference'], label='Seasonal Differencing')
plt.title('Seasonal Differencing')
plt.xlabel('Month')
plt.ylabel('Difference')
plt.legend()

plt.tight_layout()
plt.show()
