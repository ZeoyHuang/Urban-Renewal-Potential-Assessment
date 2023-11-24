# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:24:29 2023

@author: Hzy
"""

import requests
from bs4 import BeautifulSoup
import csv

# Replace with the actual URL you intend to scrape from
URL = 'http://example.com/residential-areas-yangpu'

# This function would send a request to the URL and parse the response
def scrape_residential_areas(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # You would need to inspect the HTML structure of the webpage to determine
    # the correct selectors for the residential area names and AOI data.
    # Below is a hypothetical example and needs to be tailored to the actual webpage:

    # Find the elements that contain the residential area names and AOI data
    residential_areas = soup.find_all('div', class_='residential-area')
    
    # List to store the scraped data
    data = []

    for area in residential_areas:
        name = area.find('h2', class_='name').text  # Hypothetical example
        # AOI data extraction logic goes here; it could be coordinates or other identifying info
        aoi = area.find('span', class_='aoi-data').text  # Hypothetical example

        data.append({'name': name, 'aoi': aoi})

    return data

# This function would write the scraped data to a CSV file
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'aoi'])
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

# Main script logic
if __name__ == '__main__':
    residential_data = scrape_residential_areas(URL)
    write_to_csv(residential_data, 'Yangpu_Residential_Areas.csv')

    print('Data scraping is complete.')