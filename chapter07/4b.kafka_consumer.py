from confluent_kafka import Consumer, KafkaError
import json
import time

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mongodb_consumer_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_config)
consumer.subscribe(['mongodb_topic'])

# Set the duration for which the consumer should run (in seconds)
run_duration = 10  # For example, 10 seconds
start_time = time.time()

print("Starting consumer...")

while True:
    # Check if the specified duration has passed
    if time.time() - start_time > run_duration:
        print("Time limit reached, shutting down consumer.")
        break

    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Reached end of partition')
        else:
            print(f'Error: {msg.error()}')
    else:
        # Process the message
        document = json.loads(msg.value().decode('utf-8'))
        print(f'Received document: {document}')
        # Add your processing logic here

consumer.close()
print("Consumer closed.")