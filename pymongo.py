from pymongo import MongoClient

# MongoDB connection parameters
mongo_params = {
    'host': 'your_mongo_host',
    'port': 27017,
    'username': 'your_mongo_username',
    'password': 'your_mongo_password',
    'authSource': 'your_auth_database'
}

# Function to check if a collection exists in the database
def collection_exists(db, collection_name):
    return collection_name in db.list_collection_names()

# Function to create a collection in the database
def create_collection(db, collection_name):
    db.create_collection(collection_name)

# Function to insert data into a collection
def insert_data(collection, data):
    collection.insert_many(data)

# Mock document data
documents = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22}
]

# MongoDB database and collection names
db_name = 'example_mongodb'
collection_name = 'example_collection'

# Connect to MongoDB
client = MongoClient(**mongo_params)
db = client[db_name]

# Check if the collection exists, and create it if it doesn't
if not collection_exists(db, collection_name):
    create_collection(db, collection_name)

# Get the collection
collection = db[collection_name]

# Insert data into the collection
insert_data(collection, documents)

# Query data from the collection
result = collection.find()
for document in result:
    print(document)

# Close the MongoDB connection
client.close()
