import pandas as pd
from datetime import datetime

# Sample dataset with timestamps
data = {
    'Timestamp': ['2023-10-25 10:00:00', '2023-10-25 11:00:00', '2023-10-25 12:00:00'],
    'Value': [50, 55, 60]
}

# Convert the 'Timestamp' column to datetime objects
df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Reference timestamp (current time for this example)
reference_timestamp = datetime(2023, 10, 25, 12, 30, 0)

# Step 1: Import necessary libraries and create the dataset
# We import Pandas and the datetime module and create a sample dataset with timestamps.

# Step 2: Convert timestamps to datetime objects
# We convert the 'Timestamp' column to datetime objects to work with timestamps effectively.

# Step 3: Define the reference timestamp
# In this example, we set a reference timestamp, which represents the current time.

# Step 4: Calculate timeliness
timeliness_check = df['Timestamp'] < reference_timestamp

# Step 5: Display timeliness results
print("Timeliness Check:")
print(timeliness_check)
