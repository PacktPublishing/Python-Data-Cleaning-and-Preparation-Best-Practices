import numpy as np
import pandas as pd

# Load the 'iris' dataset from seaborn library
iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

iris_data.to_csv('great_expectations/iris_data.csv', index=False)
print("File written! :)")