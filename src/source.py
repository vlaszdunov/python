import requests
from bs4 import BeautifulSoup as bs
import re
import os

URL = 'https://www.python.org/downloads/'

request_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
}
# get list of active releases
response = requests.get(URL, request_headers).text

page_data = bs(response, 'lxml')

actual_versions_raw_list = page_data.find_all(
    'span', attrs={'class': 'release-version'})

active_releases_list = []
for span in actual_versions_raw_list:
    active_releases_list.append(span.text)

active_releases_list = active_releases_list[2:]

# get all stable releases
response = requests.get(f'{URL}source/', request_headers).text
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
print(active_releases_list)
Dockerfile_temp = open('Dockerfile.template').read()
if os.path.exists('Python_dockerfiles') == False:
    os.mkdir('Python_dockerfiles')
for version in active_releases_list:
    if re.fullmatch(r'\d.*', version):
        os.mkdir(f'Python_dockerfiles/{version}')
        open(f'Python_dockerfiles/{version}/tags.txt', 'w').write(version)
        
for link in actual_stable_releases_links:
    py_version = re.search(r'\d+.\d+.?\d*', link)[0]  # type:ignore
    py_short_version = re.search(r'\d+.\d+', py_version)[0]  # type:ignore
    Dockerfile = Dockerfile_temp.format(python_link=link,
                                        python_version=py_version,
                                        python_short_version=py_short_version)

    open(
        f'Python_dockerfiles/{py_short_version}/Dockerfile', 'w').write(Dockerfile)
    open(f'Python_dockerfiles/{py_short_version}/tags.txt', 'a')\
        .write(f'\n{py_version}')

    if actual_stable_releases_links.index(link) == 0:
        ver_short_version = re.sub(r'\.\d*', '', py_short_version)
        open(f'Python_dockerfiles/{py_short_version}/tags.txt',
             'a').write(f'\n{ver_short_version}')
        open(f'Python_dockerfiles/{py_short_version}/tags.txt',
             'a').write(f'\nlatest')
