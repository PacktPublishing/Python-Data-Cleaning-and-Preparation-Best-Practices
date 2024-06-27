import time
import random

# Step 1: Generate Mock Data Continuously
def generate_mock_data():
    while True:
        record = {
            'id': random.randint(1, 1000),
            'value': random.random() * 100
        }
        yield record
        time.sleep(0.5)  # Simulate data arriving every 0.5 seconds

# Step 2: Stream Processing
def process_stream():
    for record in generate_mock_data():
        transformed_record = transform_data(record)
        load_data(transformed_record)

# Step 3: Transform Data
def transform_data(record):
    transformed_record = {
        'id': record['id'],
        'value': record['value'],
        'transformed_value': record['value'] * 1.1  # Example transformation
    }
    return transformed_record

# Step 4: Load Data
def load_data(record):
    # Simulate loading data into a database
    print(f"Loading record into database: {record}")

# Main Function
def main():
    process_stream()

if __name__ == "__main__":
    main()
