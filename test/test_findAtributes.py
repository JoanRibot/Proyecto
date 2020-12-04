from src.programa import buscaAtributos

atributo="tiempo"
html="<body><p class='sol'>hace sol</p>"

assert buscaAtributos(html, atributo)=="hace sol"

