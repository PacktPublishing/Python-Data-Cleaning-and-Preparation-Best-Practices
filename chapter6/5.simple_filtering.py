import pandas as pd

# Sample sales data
data = {
    'Category': ['Electronics', 'Electronics', 'Furniture', 'Furniture', 'Clothing', 'Clothing'],
    'Sub-Category': ['Mobile', 'Laptop', 'Chair', 'Table', 'Men', 'Women'],
    'Sales': [100, 200, 150, 300, 120, 180],
    'Quantity': [10, 5, 8, 3, 15, 12],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
}
df = pd.DataFrame(data)

# Filter to show products with quantity > 10
filtered_data = df[df['Quantity'] > 10]

print("Filtered Data:")
print(filtered_data)
