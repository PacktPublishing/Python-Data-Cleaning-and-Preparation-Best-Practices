from pymongo import MongoClient

# MongoDB connection parameters
mongo_params = {
    'host': 'localhost',
    'port': 27017,
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

# Mock document data with different structures
documents = [
    {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
    {'name': 'Bob', 'age': 30, 'address': '123 Main St'},
    {'name': 'Charlie', 'age': 22, 'hobbies': ['reading', 'gaming']},
    {'name': 'David', 'age': 40, 'email': 'david@example.com', 'address': '456 Elm St', 'active': True},
    {'name': 'Eve', 'age': 35, 'email': 'eve@example.com', 'phone': '555-1234'}
]

# MongoDB database and collection names
db_name = 'no_sql_db'
collection_name = 'best_collection_ever'

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
