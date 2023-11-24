# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:13:31 2023

@author: Hzy
"""

import pandas as pd
import requests
from urllib.parse import urlencode

# Define the base URL for the Nominatim API
NOMINATIM_API_URL = "https://nominatim.openstreetmap.org/search?"

# Function to get the coordinate value for an address
def get_coordinates(address):
    # Set up the parameters for the API request
    params = {
        'q': address,
        'format': 'json'
    }
    
    # Send a GET request to the Nominatim API
    response = requests.get(NOMINATIM_API_URL + urlencode(params), headers={'User-Agent': 'OpenAI GPT-3 example script'})
    
    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        if results:
            # Extract the latitude and longitude from the first result
            lat = results[0]['lat']
            lon = results[0]['lon']
            return lat, lon
    return None, None

# Read the input CSV file
df = pd.read_csv('List of Historic Buildings & Historic Preservation Area.csv')

# Prepare the output DataFrames
historic_buildings_poi = pd.DataFrame(columns=['Address', 'Latitude', 'Longitude'])
historic_areas_poi = pd.DataFrame(columns=['Address', 'Latitude', 'Longitude'])

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Get the coordinates for the address
    latitude, longitude = get_coordinates(row['Address Name'])
    
    # Depending on the category, append the data to the appropriate DataFrame
    if row['Category'] == 'Historic Buildings':
        historic_buildings_poi = historic_buildings_poi.append({'Address': row['Address Name'], 'Latitude': latitude, 'Longitude': longitude}, ignore_index=True)
    elif row['Category'] == 'Historic Preservation Area':
        historic_areas_poi = historic_areas_poi.append({'Address': row['Address Name'], 'Latitude': latitude, 'Longitude': longitude}, ignore_index=True)

# Write the output DataFrames to CSV files
historic_buildings_poi.to_csv('Historic Buildings_POI.csv', index=False)
historic_areas_poi.to_csv('Historic Preservation Area_POI.csv', index=False)