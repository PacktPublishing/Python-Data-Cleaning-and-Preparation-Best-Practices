import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Create time-based features
data['Day_of_Week'] = data.index.dayofweek

# Set the day of the week as a categorical variable for proper ordering in the box plot
data['Day_of_Week'] = pd.Categorical(data['Day_of_Week'], categories=range(7), ordered=True)

# Plot the original time series and the added time-based features
plt.figure(figsize=(12, 6))
plt.plot(data['Passengers'], label='Original Data', color='blue')

# Highlight certain time-based features
scatter = plt.scatter(data.index, data['Passengers'], c=data['Day_of_Week'], cmap='viridis', label='Day of Week', marker='o')

plt.title('Airline Passenger Dataset with Time-Based Features')
plt.xlabel('Month')
plt.ylabel('Number of Passengers')
plt.legend()
plt.colorbar(scatter, label='Day of Week', ticks=np.arange(7), format='%1.0f')
plt.show()
# Create a box plot to visualize the distribution of passenger numbers for each day of the week
plt.figure(figsize=(12, 6))
sns.boxplot(x='Day_of_Week', y='Passengers', data=data, palette='viridis')

plt.title('Distribution of Passenger Numbers by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Passengers')
plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.show()
