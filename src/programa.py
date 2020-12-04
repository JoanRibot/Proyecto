from htmlString import htmls

def buscaAtributos(htmlPais, atributo):
    buscar = htmlPais.find(atributo)
    if buscar == -1:
        return None, 0
    desde = htmlPais.find('>', buscar)         
    hasta = htmlPais.find('<', desde)               
    encontrado = htmlPais[desde + 1 : hasta]
    htmlPais = htmlPais[hasta:] 
    return encontrado, htmlPais

def menuCompleto(Atributos,html):
    diccionario={}
    resto=""
    for i in Atributos:
        nombre, resto = buscaAtributos(html, i)
        if nombre == None:
            return None, 0
        diccionario[i] = nombre
    return diccionario, resto

def menusCompletos(html, Atributos):
    resto = html
    count = 0
    menusPagina = {}
    while True:
        diccionario, resto = menuCompleto(Atributos, resto)
        if diccionario == None:
            break
        menusPagina[count] = diccionario
        count += 1
    return menusPagina


def BuscaMenu(htmls):
    Atributos = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]
    paises = ["China", "España", "Tailandia", "Mexico", "Italia","Francia"]
    count = 0
    jason = {}
    for i in htmls:
        menus = menusCompletos(i,Atributos)
        jason[paises[count]] = menus
        count += 1
    return jason
            
print(BuscaMenu(htmls))
