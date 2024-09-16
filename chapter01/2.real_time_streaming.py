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

# Step 2: Stream Processing with a time limit
def process_stream(run_time_seconds=10):
    start_time = time.time()
    for record in generate_mock_data():
        transformed_record = transform_data(record)
        load_data(transformed_record)
        
        # Check if the run time has exceeded the limit
        if time.time() - start_time > run_time_seconds:
            print("Time limit reached. Terminating the stream processing.")
            break

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
    process_stream(run_time_seconds=10)  # Run the stream for 10 seconds

if __name__ == "__main__":
    main()
