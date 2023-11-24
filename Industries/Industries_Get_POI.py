# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:20:11 2023

@author: Hzy
"""

import requests
import csv
import pandas as pd

# Replace with your actual API key for the service you choose to use
API_KEY = 'YOUR_API_KEY'

# Base URL for the place search request (This is a placeholder for Google Places API)
PLACE_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

# Define the search queries for each category of POI
categories = {
    'Factory': 'factories in Yangpu District, Shanghai',
    'Company': 'companies in Yangpu District, Shanghai',
    'Enterprise': 'enterprises in Yangpu District, Shanghai'
}

# Function to get POI data for a category
def get_pois_for_category(category, query):
    params = {
        'query': query,
        'key': API_KEY
    }

    response = requests.get(PLACE_SEARCH_URL, params=params)
    response_data = response.json()

    # Check if the API call was successful
    if response_data['status'] == 'OK':
        # Extract the POIs from the response
        pois = response_data['results']
        # Extract the needed data
        poi_data = [
            {
                'Name': poi['name'],
                'Address': poi['formatted_address'],
                'Latitude': poi['geometry']['location']['lat'],
                'Longitude': poi['geometry']['location']['lng']
            }
            for poi in pois
        ]
        return poi_data
    else:
        print(f"Error fetching POI data for {category}: {response_data['status']}")
        return []

# Iterate over each category and fetch POI data
for category, query in categories.items():
    poi_data = get_pois_for_category(category, query)
    # Create a DataFrame from the POI data
    df = pd.DataFrame(poi_data)
    # Write the DataFrame to a CSV file
    df.to_csv(f'{category}_POI.csv', index=False)

print('POI data fetching is complete.')