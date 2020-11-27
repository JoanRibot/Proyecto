from requests_html import HTMLSession

html= HTMLSession()
page=html.get("https://joanribot.github.io/Proyecto/")
page_text=page.text


def findMenu(x):
    buscaClase = html.find("menuCompleto") #Esto dará un número donde se encuentra "menuCompleto"
    desde = html.find(">", buscaClase) #Empezará desde ">" desde la posición número "menuCompleto"
    hasta = html.find("<", desde) #Acabará cuando encuentre el siguiente "<" desde la posición "desde"
    menu = html[desde + 1 : hasta] #El html será todo aquello que se encuentre entre ">" y "<"
    return menu

def findPlato1(html):
    buscaClase = html.find("plato1")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    primerPlato = html[desde + 1 : hasta]
    return primerPlato

def findPlato2(html):
    buscaClase = html.find("plato2")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    segundoPlato= html[desde + 1 : hasta]
    return segundoPlato

def findPlato3(html):
    buscaClase = html.find("plato3")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    tercerPlato = html[desde + 1 : hasta]
    return tercerPlato
    
def bebida(html):
    buscaClase = html.find("plato4")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    bebida = html[desde + 1 : hasta]
    return bebida

def findStock(html):
    buscaClase = html.find("stck")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    stock = html[desde + 1 : hasta]
    return stock

def findPrice(html):
    buscaClase = html.find("price")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    precio = html[desde + 1 : hasta]
    return precio

def buscarAtributo(html,x):
    buscaClase = html.find(x)
    if buscaClase==-1:
        return None,0
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    valoracion = html[desde + 1 : hasta]
    html=html[hasta:]
    return valoracion, html

Buscados=["menuCompleto", "plato1", "plato2", "plato3", "bebida","stck","price","valoration"]
def buscaAtributos(html,Buscados):
    coleccion={}
    while True:
        for i in Buscados:
            coleccion[i]=buscarAtributo(html,i)
    return coleccion

print(buscaAtributos(page_text,Buscados))


