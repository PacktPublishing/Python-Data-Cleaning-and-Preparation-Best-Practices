import pandas as pd

# Sample sales data
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing'],
    'Sub-Category': ['Mobile', 'Laptop', 'Chair', 'Table', 'Men', 'Women'],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': [200, 300, 150, 350, 100, 250],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
}

df = pd.DataFrame(data)
print(df)
