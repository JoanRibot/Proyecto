from src.programa import busca_atributo
import pytest

def test_busca_atributos():
    busca_atributo("tiempo","<body><p class='tiempo'>hace sol</p>") == "hace sol"