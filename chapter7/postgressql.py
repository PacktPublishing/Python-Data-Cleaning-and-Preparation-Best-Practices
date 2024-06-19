import pandas as pd
import psycopg2
from psycopg2 import sql

# Function to check if a table exists in the database
def table_exists(cursor, table_name):
    cursor.execute(
        sql.SQL("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)"),
        [table_name]
    )
    return cursor.fetchone()[0]

# Function to create a table in the database
def create_table(cursor, table_name):
    cursor.execute(
        sql.SQL("""
            CREATE TABLE {} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                age INT
            )
        """).format(sql.Identifier(table_name))
    )

# Function to insert data into the table
def insert_data(cursor, table_name, data):
    cursor.executemany(
        sql.SQL("INSERT INTO {} (name, age) VALUES (%s, %s)").format(sql.Identifier(table_name)),
        data
    )

# Mock DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 22]
}

df = pd.DataFrame(data)

# PostgreSQL connection parameters
db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

# Connect to PostgreSQL
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Specify the table name
table_name = 'example_table'

# Check if the table exists, and create it if it doesn't
if not table_exists(cursor, table_name):
    create_table(cursor, table_name)

# Insert data into the table
insert_data(cursor, table_name, df.values.tolist())

# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()
