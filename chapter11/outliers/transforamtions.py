import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample sales revenue dataset with extreme values
sales_data = pd.Series([100, 150, 200, 300, 500, 800, 1200, 2000, 3000, 5000, 8000, 12000])

# Logarithmic transformation
log_transformed_data = np.log(sales_data)

# Plotting the original and transformed data with shifted axis
fig, ax1 = plt.subplots(figsize=(10, 5))

color = 'skyblue'
ax1.set_xlabel('Data Point')
ax1.set_ylabel('Sales Revenue', color=color)
ax1.plot(sales_data, marker='o', color=color, linestyle='--', label='Original Data')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'lightcoral'
ax2.set_ylabel('Log(Sales Revenue)', color=color)
ax2.plot(log_transformed_data, marker='x', color=color, linestyle='-', label='Log-Transformed Data')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # ensure no overlapping of plots
plt.title('Original and Log-Transformed Sales Revenue Data')
plt.show()

# Original Data
print("Descriptive Statistics - Original Data:")
print(sales_data.describe())

# Log-Transformed Data
print("\nDescriptive Statistics - Log-Transformed Data:")
print(log_transformed_data.describe())

plt.figure(figsize=(12, 6))

# Original Data Histogram
plt.subplot(1, 2, 1)
plt.hist(sales_data, bins=10, color='skyblue', edgecolor='black')
plt.title('Original Sales Revenue Data')
plt.xlabel('Sales Revenue')
plt.ylabel('Frequency')

# Log-Transformed Data Histogram
plt.subplot(1, 2, 2)
plt.hist(log_transformed_data, bins=10, color='lightcoral', edgecolor='black')
plt.title('Log-Transformed Sales Revenue Data')
plt.xlabel('Log(Sales Revenue)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()




plt.figure(figsize=(10, 6))

# Original Data Box Plot
plt.subplot(1, 2, 1)
plt.boxplot(sales_data, vert=False)
plt.title('Original Sales Revenue Data')
plt.xlabel('Sales Revenue')

# Log-Transformed Data Box Plot
plt.subplot(1, 2, 2)
plt.boxplot(log_transformed_data, vert=False)
plt.title('Log-Transformed Sales Revenue Data')
plt.xlabel('Log(Sales Revenue)')

plt.tight_layout()
plt.show()

