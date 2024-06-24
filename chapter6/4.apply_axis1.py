import pandas as pd
import numpy as np

# Sample sales data with additional columns
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing'],
    'Sub-Category': ['Mobile', 'Laptop', 'Chair', 'Table', 'Men', 'Women'],
    'Sales': [100, 200, 150, 300, 120, 180],
    'Quantity': [10, 5, 8, 3, 15, 12],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
}
df = pd.DataFrame(data)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define a function to compute Total_Sales_Quantity and Sales_Quantity_Ratio
def compute_metrics(row):
    total_sales_quantity = row['Sales'] + row['Quantity']
    sales_quantity_ratio = row['Sales'] / row['Quantity'] if row['Quantity'] != 0 else np.nan
    return pd.Series([total_sales_quantity, sales_quantity_ratio], index=['Total_Sales_Quantity', 'Sales_Quantity_Ratio'])

# Apply the function row-wise (axis=1) to calculate new metrics
df[['Total_Sales_Quantity', 'Sales_Quantity_Ratio']] = df.apply(compute_metrics, axis=1)

# Group by 'Category' to calculate metrics per category
category_metrics = df.groupby('Category')[['Total_Sales_Quantity', 'Sales_Quantity_Ratio']].mean().reset_index()

print("DataFrame with Total_Sales_Quantity and Sales_Quantity_Ratio per Category:")
print(category_metrics)
