import pytest
from src.version_parser import *

BASE_URL = 'https://www.python.org/'


def test_get_page_content():
    page_content = get_page_content(BASE_URL)
    assert len(page_content.contents) != 0
