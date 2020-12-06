from html_string import htmls
import pymongo

try:
    uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.8i6ry.mongodb.net/test"
    client = pymongo.MongoClient(uri)
    client.server_info()
    print ("Conectado al servidor %s")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print( "Error al conectar al servidor %s") % error
except pymongo.errors.CollectionInvalid as error:
    print("could not connect to MongoDB %s") % error

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
    diccionario={}
    resto=""
    for i in Atributos:
        nombre, resto = busca_atributo(html, i)
        if nombre == None:
            return None, 0
        diccionario[i] = nombre
    return diccionario, resto

def menus_completos(html, Atributos):
    resto = html
    count = 0
    menusPagina = {}
    while True:
        diccionario, resto = menu_completo(Atributos, resto)
        if diccionario == None:
            break
        menusPagina[count] = diccionario
        count += 1
    return menusPagina


def busca_menu(htmls):
    Atributos = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]
    paises = ["China", "España", "Tailandia", "Mexico", "Italia", "Francia"]
    count = 0
    jason = {}
    for i in htmls:
        menus = menus_completos(i,Atributos)
        jason[paises[count]] = menus
        count += 1
    return jason

jason = busca_menu(htmls)
print(jason)

try:
    base_datos = client.proyecto
    diccionario_json = base_datos.diccionario
    result = diccionario_json.insert_one(jason)
except Exception as error:
    print("error saving data")