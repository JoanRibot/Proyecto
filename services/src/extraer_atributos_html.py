from typing import Collection
from .html_string import htmls
from .conexion_bd import subir_json_bd


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
    platos=[]
    for i in Atributos:
        if i.find('plato') != -1:
            nombre, resto = busca_atributo(html, i)
            platos.append(nombre)
            if len(platos) ==4:
                diccionario['platos']=platos
        else:
            nombre, resto = busca_atributo(html, i)
            if nombre == None:
                return None, 0
            nombre, resto = busca_atributo(html, i)
            diccionario[i] = nombre

    assert isinstance(diccionario, Collection)

    return diccionario, resto

def menus_completos(htmls, Atributos):

    assert isinstance(Atributos, list)
    assert isinstance(htmls, list)

    for i in htmls:
        pais, resto = busca_atributo(i, "lugar")
        while True:
            diccionario, i = menu_completo(Atributos, i)
            if diccionario == None:
                break
            diccionario["lugar"] = pais
            subir_json_bd(diccionario)  




# def sube_colecciones(htmls,Atributos):

#     assert isinstance(Atributos, list)
#     assert isinstance(htmls, list)
#     for i in htmls:
#         pais,resto = busca_atributo(i, "lugar")
#         json = {}
#         if pais == None:
#             continue
#         menus = menus_completos(resto,Atributos)
#         json[pais] = menus
#         subir_json_bd(json)    
#         json.pop(pais)

#         assert isinstance(json,Collection)

 