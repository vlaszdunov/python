import requests
from bs4 import BeautifulSoup as bs
import re

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
    if '.tar.xz' not in link.get('href') and '.tgz' in link.get('href'):
        stable_releases_links.append(link.get('href'))

actual_stable_releases = []
stable_releases_links = re.findall(
    r'.*/\d*.\d*.?\d*/Python-\d*.\d*.?\d*.tgz', str(stable_releases_links))[0].replace('\'', '').split(', ')
stable_releases_links[0] = stable_releases_links[0][1:]

for link in stable_releases_links:
    if re.sub(r'.?\d*/Python.*', '', link)[34:] in actual_releases_list:
        actual_stable_releases.append(link)
# print(*stable_releases_links, sep='\n')
print(actual_stable_releases)
print(actual_releases_list)
