import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate hypothetical sales data
np.random.seed(42)
sales_data = np.random.normal(loc=1000, scale=300, size=1000)

# Plotting the distribution
plt.figure(figsize=(10, 6))
sns.histplot(sales_data, bins=30, kde=True, color='skyblue')
plt.title('Distribution of Daily Sales Revenue')
plt.xlabel('Sales Revenue')
plt.ylabel('Frequency')
plt.show()
