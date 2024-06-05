from pathlib import Path

import pytest

from src.version_parser import *

BASE_URL = 'https://www.python.org/'
correct_test_download_links = ['https://www.python.org/ftp/python/3.11.5/Python-3.11.4.tgz',\
                              'https://www.python.org/ftp/python/3.11.5/Python-3.11.9.tgz']

test_active_version_page = bs(Path('tests/test_active_versions.html')
                              .read_text(), 'lxml')
test_download_links_page = bs(Path('tests/test_download_link.html')
                              .read_text(), 'lxml')


def test_get_page_content():
    page_content = get_page_content(BASE_URL)
    assert len(page_content.contents) != 0


def test_get_active_versions():
    actual_versions = get_active_versions(test_active_version_page)
    assert actual_versions == ['3.11']


def test_get_stable_releases_link():
    active_versions_links = get_stable_releases_links(
        test_download_links_page, ['3.11'])
    assert active_versions_links == correct_test_download_link

def test_get_newest_releases_links():
    latest_releases_links = get_newest_releases_links(correct_test_download_links)
    assert latest_releases_links == ['https://www.python.org/ftp/python/3.11.5/Python-3.11.9.tgz']