import requests
from bs4 import BeautifulSoup as bs
import re

URL = 'https://www.python.org/downloads/'

# get list of active releases
response = requests.get(URL).text

page_data = bs(response, 'lxml')
actual_versions_raw_list = page_data.find_all(
    'span', attrs={'class': 'release-version'})

active_releases_list = []
for span in actual_versions_raw_list:
    active_releases_list.append(span.text)


# get all stable releases
response = requests.get(f'{URL}source/').text
page_data = bs(response, 'lxml')
releases_raw_download_links = page_data.find_all('a')

releases_download_links = []
for link in releases_raw_download_links:
    releases_download_links.append(link.get('href'))


actual_stable_releases_links = []

for actual_release in active_releases_list:
    for link in releases_download_links:
        check = re.fullmatch(r'.*Python-\d*.\d*.?\d*.tgz', link)
        if check:
            if actual_release in re.sub(r'.?\d*/Python*', '', link):
                actual_stable_releases_links.append(link)
                break

Dockerfile_temp = open('Dockerfile.template').read()
for link in actual_stable_releases_links:
    py_version = re.search(r'\d+.\d+.?\d*', link)[0]
    py_short_version = re.search(r'\d+.\d+', py_version)[0]
    Dockerfile = Dockerfile_temp.format(python_link=link,
                                   python_version=py_version,
                                   python_short_version=py_short_version)
    open(f'Dockerfile_{py_version}','w').write(Dockerfile)
