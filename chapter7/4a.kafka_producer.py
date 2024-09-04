from pymongo import MongoClient
from confluent_kafka import Producer
import json

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['no_sql_db']
collection = db['best_collection_ever']

# Kafka producer configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092'
}
producer = Producer(kafka_config)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Read from MongoDB and produce to Kafka
for document in collection.find():
    # Convert MongoDB document to JSON string
    message = json.dumps(document, default=str)
    
    # Produce message to Kafka
    producer.produce('mongodb_topic', value=message.encode('utf-8'), callback=delivery_report)
    producer.poll(0)

producer.flush()