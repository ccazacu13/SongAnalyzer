import requests
import re
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the webpage
url = 'https://genius.com'  # Replace with the target URL
response = requests.get(url)

if response.status_code == 200:
    # Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    a_tag = soup.find_all('a', href=re.compile(r'https://genius\.com/[^a/].+lyrics'))

    for tag in a_tag:
        print(tag['href'])