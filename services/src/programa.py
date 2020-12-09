<<<<<<< HEAD
from .html_string import htmls
=======
from typing import Collection
from html_string import htmls
>>>>>>> 5ba1e6efacb53c23ba4d6996411bb6a59d7a0e82

Atributos = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]

def busca_atributo(htmlPais, atributo):
    assert isinstance(htmlPais, str)
    assert isinstance(atributo, str)

    buscar = htmlPais.find(atributo)
    if buscar == -1:
        return None, 0
    desde = htmlPais.find('>', buscar)         
    hasta = htmlPais.find('<', desde)               
    encontrado = htmlPais[desde + 1 : hasta]
    htmlPais = htmlPais[hasta:]
    
    assert isinstance(encontrado, str) 
    assert isinstance(htmlPais, str) 
    return encontrado, htmlPais

def menu_completo(Atributos,html):
    assert isinstance(Atributos, list)
    assert isinstance(html, str)

    diccionario = {}
    resto = ""
    for i in Atributos:
        nombre, resto = busca_atributo(html, i)
        if nombre == None:
            return None, 0
        diccionario[i] = nombre

    assert isinstance(diccionario, Collection)
    return diccionario, resto

def menus_completos(html, Atributos):
    assert isinstance(Atributos, list)
    assert isinstance(html, str)

    resto = html
    count = 1
    menusPagina = {}
    while True:
        diccionario, resto = menu_completo(Atributos, resto)
        if diccionario == None:
            break
        menusPagina["menu" + str(count)] = diccionario
        count += 1

    assert isinstance(menusPagina, Collection)
    return menusPagina


def busca_menu(htmls,Atributos):
    assert isinstance(Atributos, list)
    assert isinstance(htmls, list)
    
    count = 0
    json = {}
    for i in htmls:
        pais,resto = busca_atributo(i, "lugar")
        if pais == None:
            continue
        menus = menus_completos(resto,Atributos)
        json[pais] = menus
        count += 1

    assert isinstance(json,Collection)
    return json

json = busca_menu(htmls,Atributos)
print(json)