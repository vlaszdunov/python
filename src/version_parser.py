import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.python.org/'
headers = json.loads(Path('src/request_header.json').read_bytes())


def get_page_content(internal_page: str = '') -> bs:
    page_content = requests.get(BASE_URL+internal_page, headers=headers).text
    return bs(page_content, 'lxml')


def get_active_versions(versions_page_internal_url: str):
    pass