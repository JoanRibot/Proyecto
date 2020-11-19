## Esto es el ejemplo de Udacity para sacar todos los links de la página

# page = ""

# def get_next_target(page):
#    start_link = page.find('<a href=')
#    
#    if start_link == -1:
#        return None, 0
    
#    start_quote = page.find('"', start_link)
#    end_quote = page.find('"', start_quote + 1)
#    html = page[start_quote + 1:end_quote]
#    return html, end_quote

# def all_links(page):
#    while True:
#        html, endpos = get_next_target(page)
#        if html:
#            print html
#            page = page[endpos:]
#        else:
#            break
from htmllib.request import htmlopen
from bs4 import BeautifulSoup

abrirPagina = htmlopen("https://joanribot.github.io/Proyecto/")
paginaHTml = BeautifulSoup(abrirPagina.read(), "html.parser")
def findNextLink(html):
    buscaClase=html.find("href")


def findMenu(html):
    buscaClase = html.find("menuCompleto") #Esto dará un número donde se encuentra "menuCompleto"
    if buscaClase == -1: #Si no hay más "clases" iguales a esta, significará que no hay más menús en esa página
        nextLink()
    desde = html.find(">", buscaClase) #Empezará desde ">" desde la posición número "menuCompleto"
    hasta = html.find("<", desde) #Acabará cuando encuentre el siguiente "<" desde la posición "desde"
    menu = html[desde + 1 : hasta] #El html será todo aquello que se encuentre entre ">" y "<"
    html=html[hasta:]
    return menu, html #Devolverá el "menu", y el "html" para seguir buscando a partir de este punto

def findPlato1(html):
    buscaClase = html.find("plato1")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    primerPlato = html[desde + 1 : hasta]
    html=html[hasta:]
    return primerPlato, html

def findPlato2(html):
    buscaClase = html.find("plato2")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    segundoPlato= html[desde + 1 : hasta]
    html=html[hasta:]
    return segundoPlato, html

def findPlato3(html):
    buscaClase = html.find("plato3")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    tercerPlato = html[desde + 1 : hasta]
    html=html[hasta:]
    return tercerPlato, html
    
def bebida(html):
    buscaClase = html.find("plato4")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    bebida = html[desde + 1 : hasta]
    html=html[hasta:]
    return bebida, html

def findStock(html):
    buscaClase = html.find("stck")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    stock = html[desde + 1 : hasta]
    html=html[hasta:]
    return stock, html

def findPrice(html):
    buscaClase = html.find("price")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    precio = html[desde + 1 : hasta]
    html=html[hasta:]
    return precio, html

def findValoration(html):
    buscaClase = html.find("valoration")
    desde = html.find(">", buscaClase)
    hasta = html.find("<", desde)
    valoracion = html[desde + 1 : hasta]
    html=html[hasta:]
    return valoracion, html

def findAll():





if __name__  ==  "__main__":
    assert findMenu(page)  ==  "Menú Dragon"
