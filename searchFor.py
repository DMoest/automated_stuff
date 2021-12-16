#! python3
# searchFor.py - Search and open several search results.

import requests
import sys
import webbrowser
import bs4

print('Searching...')   # Display while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res. raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElements = soup.select('.package-snippet')
numOpen = min(5, len(linkElements))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElements[i].get('href')
    print('Opening ', urlToOpen)
    webbrowser.open(urlToOpen)
