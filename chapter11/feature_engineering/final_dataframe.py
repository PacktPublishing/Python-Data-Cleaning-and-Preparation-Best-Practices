import pandas as pd

# Load the airline passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Create time-based features
data['Day_of_Week'] = data.index.dayofweek
data['Month'] = data.index.month
data['Quarter'] = data.index.quarter
data['Year'] = data.index.year

# Compute first-order differences
data['Differences'] = data['Passengers'].diff()

# Compute second-order differences
data['Second_Order_Differences'] = data['Passengers'].diff().diff()

# Display the final dataframe
print(data.head())
