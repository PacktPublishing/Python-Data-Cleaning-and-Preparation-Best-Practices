import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

# Create a base directory for storing partitioned data
base_directory = "/Users/maria.zervou/projects/python_best_practices/data_sinks/hybrid_data"

# Hybrid partitioning
hybrid_data = {"timestamp": ["2022-01-01", "2022-01-01", "2022-01-02"],
               "region": ["North", "South", "East"],
               "value": [10, 15, 12]}
hybrid_df = pd.DataFrame(hybrid_data)

for (timestamp, region), group in hybrid_df.groupby(["timestamp", "region"]):
    # Create a directory for each timestamp and region combination within the base directory
    timestamp_path = os.path.join(base_directory, str(timestamp))
    os.makedirs(timestamp_path, exist_ok=True)
    timestamp_region_path = os.path.join(base_directory, str(timestamp), str(region))
   
    # Convert the group to a PyArrow Table and write it to the partition path
    table = pa.Table.from_pandas(group)
    pq.write_table(table, timestamp_region_path)

