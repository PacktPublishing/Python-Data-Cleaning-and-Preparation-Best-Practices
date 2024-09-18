def read_sql():
    # Simulating a SQL table with a dictionary
    sql_table = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 24},
    ]
    for row in sql_table:
        process_row(row)

def process_row(row):
    print(f"Processing row: id={row['id']}, name={row['name']}, age={row['age']}")

# Example usage
read_sql()

print(f"{'id':<5} {'name':<10} {'age':<3}")
print("-" * 20)
# Print each row
for row in sql_table:
print(f"{row['id']:<5} {row['name']:<10} {row['age']:<3}")
