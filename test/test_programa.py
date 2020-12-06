from src.programa import buscaAtributos

import pytest

@pytest.mark.buscaAtributos
def test_buscaAtributos():
    assert buscaAtributos("<body><p class='tiempo'>hace sol</p>", "tiempo")== "hace sol", "</p>"

