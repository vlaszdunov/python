import pytest

from src.version_parser import *

BASE_URL = 'https://www.python.org/'


def test_get_page_content():
    page_content = get_page_content(BASE_URL)
    assert len(page_content.contents) != 0


def test_get_versions():
    # Проверяем, что функция get_versions() использует результаты get_data()
    actual_versions = get_active_versions('downloads/')
    # Предположим, что это версии, которые мы ожидаем получить
    assert actual_versions.__class__==list
