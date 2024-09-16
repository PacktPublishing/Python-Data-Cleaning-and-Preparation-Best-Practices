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
