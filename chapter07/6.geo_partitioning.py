import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

# Create a base directory for storing partitioned data
base_directory = "/Users/maria.zervou/projects/python_best_practices/data_sinks/geo_data"
os.makedirs(base_directory, exist_ok=True)

# Geographic partitioning
geo_data = {"region": ["North", "South", "East"],
            "value": [10, 15, 12]}
geo_df = pd.DataFrame(geo_data)

for region, group in geo_df.groupby("region"):
    # Create a directory for each region within the base directory
    region_path = os.path.join(base_directory, region)
    
    # Convert the group to a PyArrow Table and write it to the partition path
    table = pa.Table.from_pandas(group)
    pq.write_table(table, region_path)
