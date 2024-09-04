import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

# Sample data
data = {"timestamp": ["2022-01-01", "2022-01-01", "2022-01-02"],
        "value": [10, 15, 12]}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Convert the timestamp column to a datetime type
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Time-based partitioning
base_path = "path_to_write_data"
for timestamp, group in df.groupby(df["timestamp"].dt.date):
    # Create the directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    
    partition_path = os.path.join(base_path, str(timestamp))
    
    table = pa.Table.from_pandas(group)
    pq.write_table(table, partition_path)

# To read data from a specific partition
specific_partition_path = "/Users/maria.zervou/projects/python_best_practices/data_sinks/data/2022-01-01"
partitioned_data = pq.read_table(specific_partition_path).to_pandas()
