from pathlib import Path

import pytest

from src.version_parser import *

BASE_URL = 'https://www.python.org/'


test_html = bs(Path('tests/test_html.html').read_text(), 'lxml')


def test_get_page_content():
    page_content = get_page_content(BASE_URL)
    assert len(page_content.contents) != 0


def test_get_versions():
    actual_versions = get_active_versions(test_html)
    assert actual_versions == ['3.11']
