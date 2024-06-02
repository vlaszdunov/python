import requests
from bs4 import BeautifulSoup as bs
import re

URL = 'https://www.python.org/downloads/'
в
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

releases_links = []
for link in stable_releases_raw_links:
    releases_links.append(link.get('href'))


actual_stable_releases_links = []

for actual_release in actual_releases_list:
    for link in releases_links:
        check = re.fullmatch(r'.*Python-\d*.\d*.?\d*.tgz', link)
        if check:
            if actual_release in re.sub(r'.?\d*/Python*', '', link):
                actual_stable_releases_links.append(link)
                break