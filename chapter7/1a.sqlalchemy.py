import pandas as pd
from sqlalchemy import create_engine, inspect, Table, Column, Integer, String, MetaData

# Function to check if a table exists
def table_exists(engine, table_name):
    inspector = inspect(engine)
    return inspector.has_table(table_name)

# Function to create a new table
def create_table(engine, table_name):
    metadata = MetaData()
    table = Table(
        table_name, metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(255)),
        Column('age', Integer)
    )
    metadata.create_all(engine)

# Function to insert data into the table
def insert_data(engine, table_name, data):
    with engine.connect() as conn:
        conn.execute(
            Table(table_name, MetaData(), autoload_with=engine)
            .insert()
            .values(data)
        )

# Mock DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22]
}
df = pd.DataFrame(data)

# Database connection parameters
db_url = 'your_database_url'  # Example: 'postgresql://user:password@localhost:5432/your_database'

# Connect to the database
engine = create_engine(db_url)

# Specify the table name
table_name = 'my_example_table'

# Check if the table exists, and create it if it doesn't
if not table_exists(engine, table_name):
    create_table(engine, table_name)

# Insert data into the table
insert_data(engine, table_name, df.to_dict(orient='records'))

# No explicit close needed as SQLAlchemy handles connection pooling and cleanup

print("Operations completed successfully.")
