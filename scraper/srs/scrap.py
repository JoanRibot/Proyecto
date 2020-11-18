#Esto es el ejemplo de Udacity para sacar todos los links de la página

#page = ""

#def get_next_target(page):
#    start_link = page.find('<a href=')
#    
#    if start_link == -1:
#        return None, 0
    
#    start_quote = page.find('"', start_link)
#    end_quote = page.find('"', start_quote + 1)
#    url = page[start_quote + 1:end_quote]
#    return url, end_quote

#def all_links(page):
#    while True:
#        url, endpos = get_next_target(page)
#        if url:
#            print url
#            page = page[endpos:]
#        else:
#            break
    

def findMenu(url):
    nombre_menu = url.find("menuCompleto") #Esto dará un número donde se encuentra "menuCompleto"
    desde = url.find(">", nombre_menu) #Empezará desde ">" desde la posición número "menuCompleto"
    hasta = url.find("<", desde) #Acabará cuando encuentre el siguiente "<" desde la posición "desde"
    menu = url[desde + 1 : hasta] #El url será todo aquello que se encuentre entre ">" y "<"
    if nombre_menu == -1: #Si no hay más "nombre_menu", significará que no hay más menús en esa página
        return menu, hasta
    return menu, hasta #Devolverá el "menu", y el "hasta" para seguir con el bucle toda la página

def findPlato1(url):
    nombre_primer_plato = url.find("plato1")
    desde = url.find(">", nombre_primer_plato)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta

def findPlato2(url):
    nombre_segundo_plato = url.find("plato2")
    desde = url.find(">", nombre_segundo_plato)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta

def findPlato3(url):
    nombre_tercer_plato = url.find("plato3")
    desde = url.find(">", nombre_tercer_plato)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta
    
def findPlato4(url):
    nombre_cuarto_plato = url.find("plato4")
    desde = url.find(">", nombre_cuarto_plato)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta

def findStock(url):
    numero_stock = url.find("stck")
    desde = url.find(">", numero_stock)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta

def findPrice(url):
    precio = url.find("price")
    desde = url.find(">", precio)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta

def findValoration(url):
    valoracion = url.find("valoration")
    desde = url.find(">", valoracion)
    hasta = url.find("<", desde)
    menu = url[desde + 1 : hasta]
    return menu, hasta






if __name__  ==  "__main__":
    assert findMenu('dnpkabefifaife <p class = "menuCompleto">Nombre del menú<p> rsoisrofsj')  ==  "Nombre del menú"
