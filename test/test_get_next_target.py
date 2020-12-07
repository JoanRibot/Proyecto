from src.html_string import get_next_target
from .htmlDePrueba import page_prueba
import pytest


@pytest.mark.get_next_target
def test_get_next_target():
    assert get_next_target(page_prueba)==('"https://joanribot.github.io/Sandbox0/enlace1.html"',248)