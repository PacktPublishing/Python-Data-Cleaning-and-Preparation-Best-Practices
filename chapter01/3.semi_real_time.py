import time
import random
from collections import deque

# Step 1: Generate Mock Data Continuously
def generate_mock_data():
    while True:
        record = {
            'id': random.randint(1, 1000),
            'value': random.random() * 100
        }
        yield record
        time.sleep(0.1)  # Simulate data arriving every 0.1 seconds

# Step 2: Process Semi-Real-Time
def process_semi_real_time(batch_size, interval):
    buffer = deque()
    start_time = time.time()

    for record in generate_mock_data():
        buffer.append(record)
        
        # Check if interval has elapsed or buffer size reached
        if (time.time() - start_time) >= interval or len(buffer) >= batch_size:
            # Process and clear the buffer
            transformed_batch = transform_data(list(buffer))  # Convert deque to list
            print(f"Batch of {len(transformed_batch)} records before loading:")
            for rec in transformed_batch:
                print(rec)
            load_data(transformed_batch)
            buffer.clear()
            start_time = time.time()  # Reset start time

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
    batch_size = 5    # Number of records to process per batch
    interval = 3.0    # Maximum time interval (in seconds) to process a batch

    process_semi_real_time(batch_size, interval)

if __name__ == "__main__":
    main()
