import time
import random

# Step 1: Generate Mock Data
def generate_mock_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'id': random.randint(1, 1000),
            'value': random.random() * 100
        }
        data.append(record)
    return data

# Step 2: Batch Processing
def process_in_batches(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Step 3: Transform Data
def transform_data(batch):
    transformed_batch = []
    for record in batch:
        transformed_record = {
            'id': record['id'],
            'value': record['value'],
            'transformed_value': record['value'] * 1.1  # Example transformation
        }
        transformed_batch.append(transformed_record)
    return transformed_batch

# Step 4: Load Data
def load_data(batch):
    for record in batch:
        # Simulate loading data into a database
        print(f"Loading record into database: {record}")

# Main Function
def main():
    # Parameters
    num_record
    s = 100  # Total number of records to generate
    batch_size = 10    # Number of records per batch

    # Generate data
    data = generate_mock_data(num_records)
    
    # Process and load data in batches
    for batch in process_in_batches(data, batch_size):
        transformed_batch = transform_data(batch)
        print("Batch before loading:")
        for record in transformed_batch:
            print(record)
        load_data(transformed_batch)
        time.sleep(1)  # Simulate time delay between batches

if __name__ == "__main__":
    main()
