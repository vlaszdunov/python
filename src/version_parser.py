import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.python.org/'
headers = json.loads(Path('src/request_header.json').read_bytes())


def get_page_content(base_url, internal_page: str = '') -> bs:
    page_content = requests.get(base_url+internal_page, headers=headers).text
    return bs(page_content, 'lxml')


def get_active_versions(page_content: bs) -> list[str]:
    active_versions_raw_list = page_content\
        .find_all('span', attrs={'class': 'release-version'})

    active_versions_list = []
    for element in active_versions_raw_list:
        if re.match(r'\d+.\d+', element.text):
            active_versions_list.append(element.text)

    return active_versions_list


def get_stable_releases_links(page_content: bs, active_versions_list: list)->list[str]:
    active_stable_releases_link = []
    stable_releases_links = page_content.find_all('a')
    for link in stable_releases_links:
        if re.fullmatch(r'.*Python-\d.\d*.?\d*.tgz', link.get('href')):
            if re.search(r'\d+.\d+', link.get('href'))[0] in active_versions_list:
                active_stable_releases_link.append(link.get('href'))

    return active_stable_releases_link


def get_newest_releases_links(active_stable_releases_link: list[str]) -> list[str]:
    pass