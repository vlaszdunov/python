import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.python.org/downloads/'

# get list of active releases
response = requests.get(URL).text

page_data = bs(response, 'lxml')
actual_versions_raw_list = page_data.find_all(
    'span', attrs={'class': 'release-version'})

actual_releases_list = []
for span in actual_versions_raw_list:
    actual_releases_list.append(span.text)


# get all stable releases
response = requests.get(f'{URL}source/').text
page_data = bs(response, 'lxml')
stable_releases_raw_links = page_data.find_all('a')

stable_releases_links = []


for link in stable_releases_raw_links:
    if link.text == 'Gzipped source tarball':
        stable_releases_links.append(link.get('href'))
