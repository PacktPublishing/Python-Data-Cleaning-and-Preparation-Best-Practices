import pandas as pd
import pyarrow.parquet as pq
import boto3
from io import BytesIO

# Mock some data (replace this with your actual data)
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Convert DataFrame to Parquet format
parquet_buffer = BytesIO()
pq.write_table(pq.Table.from_pandas(df), parquet_buffer)

# AWS credentials and S3 bucket information
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
bucket_name = 'your-s3-bucket'
file_key = 'example_data.parquet'  # The key (path) of the file in S3

# Create a connection to S3
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Upload the Parquet file to S3
s3.put_object(Body=parquet_buffer.getvalue(), Bucket=bucket_name, Key=file_key)

print(f"File '{file_key}' uploaded to S3 bucket '{bucket_name}'.")
