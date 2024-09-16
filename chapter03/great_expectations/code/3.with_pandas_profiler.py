import pandas as pd
from ydata_profiling import ProfileReport

# Load the 'iris' dataset from seaborn library
iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Then run Pandas Profiling
profile = ProfileReport(iris_data, title="Pandas Profiling Report", explorative=True)

# And obtain an Expectation Suite from the profile report
suite = profile.to_expectation_suite(suite_name="my_pandas_profiling_suite")
