import numpy as np
import pandas as pd

# Load the 'iris' dataset from seaborn library
iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# do some transformtions that will fail the expectations
#update values
iris_data['sepal_length'] = 60

#rename columns
iris_data.rename(columns={'petal_width': 'petal_w'}, inplace=True)

#write dataframe
iris_data.to_csv('great_expectations/iris_data_test.csv', index=False)
print("File written! :)")