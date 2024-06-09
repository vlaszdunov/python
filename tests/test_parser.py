from pathlib import Path

import pytest

from src.version_parser import *

BASE_URL = 'https://www.python.org/'
correct_test_download_links = ['https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz',
                               'https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz']

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
    assert active_versions_links == correct_test_download_links


def test_grouping_releases_by_major_version():
    latest_releases_links = group_releases_by_major_version(
        correct_test_download_links, ['3.11'])
    print(latest_releases_links)
    assert latest_releases_links == {
        '3.11': correct_test_download_links}
