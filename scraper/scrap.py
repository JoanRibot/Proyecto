def findMenu(html):
    buscar=html.find("menuCompleto")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu

def findPlato1(html):
    buscar=html.find("plato1")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu

def findPlato2(html):
    buscar=html.find("plato2")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu

def findPlato3(html):
    buscar=html.find("plato3")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu
    
def findPlato4(html):
    buscar=html.find("plato4")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu

def findStock(html):
    buscar=html.find("stck")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu

def findPrice(html):
    buscar=html.find("price")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu

def findValoration(html):
    buscar=html.find("valoration")
    desde=html.find(">",buscar)
    hasta=html.find("<",desde)
    menu=html[desde+1:hasta]
    return menu






if __name__ == "__main__":
    assert findMenu('dnpkabefifaife <p class="menuCompleto">Nombre del menú<p> rsoisrofsj') == "Nombre del menú"
