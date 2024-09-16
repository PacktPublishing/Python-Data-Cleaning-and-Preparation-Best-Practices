def read_nosql():
    data_store = {
        "1": {"name": "Alice", "age": 30},
        "2": {"name": "Bob", "age": 24},
    }
    for key, value in data_store.items():
        process_entry(key, value)

def process_entry(key, value):
    print(f"Processing key: {key} with value: {value}")

# Example usage
read_nosql()
