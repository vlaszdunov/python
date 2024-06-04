import json
from pathlib import Path
import re

import requests
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.python.org/'
headers = json.loads(Path('src/request_header.json').read_bytes())


def get_page_content(internal_page: str = '') -> bs:
    page_content = requests.get(BASE_URL+internal_page, headers=headers).text
    return bs(page_content, 'lxml')


def get_active_versions(internal_url: str) -> list[str]:
    page_content = get_page_content(internal_url)
    active_versions_raw_list = page_content.find_all(
        'span', attrs={'class': 'release-version'})

    active_versions_list = []
    for element in active_versions_raw_list:
        if re.match(r'\d+.\d+', element.text):
            active_versions_list.append(element.text)

    return active_versions_list
