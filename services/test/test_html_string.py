from services.src.html_string  import get_next_target, all_links, crawl_web
from .htmlDePrueba import page_prueba, page_prueba2, page_prueba3

import pytest

@pytest.mark.get_next_target
def test_get_next_target():
    assert get_next_target(page_prueba) == ('"https://joanribot.github.io/Sandbox0/enlace1"',243)
    assert get_next_target(page_prueba2) == ('"https://joanribot.github.io/Sandbox0"',292)
    assert get_next_target(page_prueba3) == ('"https://joanribot.github.io/Sandbox0"',911)

@pytest.mark.all_links
def test_all_links():
    assert all_links(page_prueba) == ['"https://joanribot.github.io/Sandbox0/enlace1"','"https://joanribot.github.io/Sandbox0/enlace2"']
    assert all_links(page_prueba2) == ['"https://joanribot.github.io/Sandbox0"','"https://joanribot.github.io/Sandbox0/enlace2"']
    assert all_links(page_prueba3) == ['"https://joanribot.github.io/Sandbox0"','"https://joanribot.github.io/Sandbox0/enlace1"','"https://joanribot.github.io/Sandbox0/enlace4"']

@pytest.mark.crawl_web
def test_crawl_web():
    assert crawl_web("https://joanribot.github.io/Proyecto") == ['https://joanribot.github.io/Proyecto', 'https://joanribot.github.io/Proyecto/Menus/francesa.html', 'https://joanribot.github.io/Proyecto/Menus/italiana.html', 'https://joanribot.github.io/Proyecto/Menus/mexicana.html', 'https://joanribot.github.io/Proyecto/Menus/tailandesa.html', 'https://joanribot.github.io/Proyecto/Menus/spain.html', 'https://joanribot.github.io/Proyecto/Menus/china.html']
 
