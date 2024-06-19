from google.cloud import bigquery
from google.cloud.bigquery import SchemaField

# Set up credentials and project ID
# Replace 'your_project_id' and 'path/to/credentials.json' with your actual values
client = bigquery.Client(project='your_project_id', credentials_path='path/to/credentials.json')

# Define the dataset and table names
dataset_name = 'your_dataset'
table_name = 'your_table'

# Define table schema (replace with your own schema)
schema = [
    SchemaField('column1', 'STRING', mode='REQUIRED'),
    SchemaField('column2', 'INTEGER', mode='NULLABLE'),
    # Add more fields as needed
]

# Check if the table exists
dataset_ref = client.dataset(dataset_name)
table_ref = dataset_ref.table(table_name)
table_exists = client.get_table(table_ref, retry=3, timeout=30, max_results=None) is not None

# Create the table if it doesn't exist
if not table_exists:
    table = bigquery.Table(table_ref, schema=schema)
    client.create_table(table)

# Insert data into the table (Mock dataset)
rows_to_insert = [
    ('value1', 1),
    ('value2', 2),
    ('value3', 3),
    # Add more rows as needed
]

# Construct the data to be inserted
data_to_insert = [dict(zip([field.name for field in schema], row)) for row in rows_to_insert]

# Perform the data insertion
errors = client.insert_rows(table, data_to_insert)

# Check for insertion errors
if errors:
    print(f"Errors occurred during data insertion: {errors}")

# Close the BigQuery client
client.close()
