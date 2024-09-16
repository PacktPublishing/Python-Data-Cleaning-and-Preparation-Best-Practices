import requests
import pandas as pd

# Define the API endpoint URL
url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

# Make the API request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the response JSON data
    data = response.json()
    
    # Check if the API response contains cocktails data
    if 'drinks' in data:
        # Create DataFrame from drinks data
        df = pd.DataFrame(data['drinks'])
        
        # Print the resulting DataFrame
        print(df.head())
    else:
        print("No drinks found.")
else:
    print(f"Failed to retrieve data from API. Status code: {response.status_code}")
