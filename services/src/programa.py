from html_string import htmls

def busca_atributo(htmlPais, atributo):
    buscar = htmlPais.find(atributo)
    if buscar == -1:
        return None, 0
    desde = htmlPais.find('>', buscar)         
    hasta = htmlPais.find('<', desde)               
    encontrado = htmlPais[desde + 1 : hasta]
    htmlPais = htmlPais[hasta:] 
    return encontrado, htmlPais

def menu_completo(Atributos,html):
    diccionario = {}
    resto = ""
    for i in Atributos:
        nombre, resto = busca_atributo(html, i)
        if nombre == None:
            return None, 0
        diccionario[i] = nombre
    return diccionario, resto

def menus_completos(html, Atributos):
    resto = html
    count = 1
    menusPagina = {}
    while True:
        diccionario, resto = menu_completo(Atributos, resto)
        if diccionario == None:
            break
        menusPagina["menu" + str(count)] = diccionario
        count += 1
    return menusPagina

Atributos = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]

def busca_menu(htmls,Atributos):
    count = 0
    json = {}
    for i in htmls:
        pais,resto = busca_atributo(i, "lugar")
        if pais == None:
            continue
        menus = menus_completos(resto,Atributos)
        json[pais] = menus
        count += 1
    return json

json = busca_menu(htmls,Atributos)
