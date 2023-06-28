import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the website
url = 'https://www.example.com'
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract relevant information
# Example: Extract all the links from the website
links = soup.find_all('a')

# Store extracted data in CSV
csv_file = 'output.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link'])
    for link in links:
        writer.writerow([link['href']])

print("Data extracted and stored in", csv_file)
