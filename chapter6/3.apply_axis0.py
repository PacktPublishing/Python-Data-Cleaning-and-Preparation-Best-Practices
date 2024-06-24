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

# Define a custom function to compute multiple statistics for 'Sales' and 'Quantity'
def compute_statistics(series):
    sum_sales = series['Sales'].sum()
    mean_sales = series['Sales'].mean()
    std_sales = series['Sales'].std()
    cv_sales = std_sales / mean_sales
    
    sum_quantity = series['Quantity'].sum()
    mean_quantity = series['Quantity'].mean()
    std_quantity = series['Quantity'].std()
    cv_quantity = std_quantity / mean_quantity
    
    return pd.Series([sum_sales, mean_sales, std_sales, cv_sales, sum_quantity, mean_quantity, std_quantity, cv_quantity],
                     index=['Sum_Sales', 'Mean_Sales', 'Std_Sales', 'CV_Sales', 
                            'Sum_Quantity', 'Mean_Quantity', 'Std_Quantity', 'CV_Quantity'])

# Group by 'Category' and apply custom function to compute statistics of 'Sales' and 'Quantity'
result_complex = df.groupby('Category').apply(compute_statistics).reset_index()

print("Using apply() for complex function (multiple statistics calculation for 'Sales' and 'Quantity'):")
print(result_complex)