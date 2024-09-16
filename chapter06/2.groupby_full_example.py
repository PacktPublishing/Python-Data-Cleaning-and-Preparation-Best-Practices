import pandas as pd

# Extended sample sales data
data = {
    'Category': [
        'Electronics', 'Electronics', 'Electronics', 'Electronics', 
        'Furniture', 'Furniture', 'Furniture', 'Furniture',
        'Clothing', 'Clothing', 'Clothing', 'Clothing', 
        'Electronics', 'Furniture', 'Clothing'
    ],
    'Sub-Category': [
        'Mobile', 'Laptop', 'Tablet', 'Laptop', 
        'Chair', 'Table', 'Desk', 'Table',
        'Men', 'Women', 'Kids', 'Men', 
        'Mobile', 'Chair', 'Women'
    ],
    'Region': [
        'North', 'South', 'East', 'West', 
        'North', 'South', 'East', 'West', 
        'North', 'South', 'East', 'West',
        'North', 'West', 'East'
    ],
    'Sales': [
        200, 300, 250, 400, 
        150, 350, 200, 400, 
        100, 250, 150, 300,
        220, 170, 270
    ],
    'Date': [
        '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', 
        '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
        '2023-01-09', '2023-01-10', '2023-01-11', '2023-01-12',
        '2023-01-13', '2023-01-14', '2023-01-15'
    ]
}

df = pd.DataFrame(data)
print("_____________")
print("Sample df is shown below")
print(df)

# Group by 'Category' and aggregate the 'Sales' column
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
print("_____________")
print("Sales per Category are shown below:")
print(category_sales)

# Group by 'Category' and 'Region' and aggregate the 'Sales' column
category_region_sales = df.groupby(['Category', 'Region'])['Sales'].sum().reset_index()
print("_____________")
print("Sales per Category and Region are shown below:")
print(category_region_sales)

# Group by 'Category' and 'Region' and apply multiple aggregation functions
print("_____________")
print("Total and Mean Sales per Category and Region are shown below:")
category_region_sales_agg = df.groupby(['Category', 'Region'])['Sales'].agg(['sum', 'mean']).reset_index()
print(category_region_sales_agg)

# Multiple column aggregations
print("_____________")
print("Multiple column aggregations:")
advanced_agg = df.groupby(['Category', 'Region']).agg({
    'Sales': ['sum', 'mean', 'count'],
    'Sub-Category': 'nunique'  # Unique count of Sub-Category
}).reset_index()
print(advanced_agg)

# ____________________________________________________________________
# Define custom aggregation functions
print("_____________")
print("Custom Aggregations:")
def range_sales(series):
    return series.max() - series.min()

def coefficient_of_variation(series):
    return series.std() / series.mean()

# Group by 'Category', 'Region', and apply multiple aggregations including custom functions
advanced_agg_custom = df.groupby('Region').agg({
    'Sales': ['sum', 'mean', 'count', range_sales, coefficient_of_variation],
    'Sub-Category': 'nunique'
}).reset_index()

# Rename columns for clarity
advanced_agg_custom.columns = [
    'Region', 'Total Sales', 'Average Sales', 'Number of Transactions',
    'Sales Range', 'Coefficient of Variation', 'Unique Sub-Categories'
]

print(advanced_agg_custom)
print(# Displaying only the specified columns
print(advanced_agg_custom[['Region',  'Total Sales', 'Sales Range', 'Coefficient of Variation', 'Unique Sub-Categories']]))



