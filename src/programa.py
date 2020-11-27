from requests_html import HTMLSession

html = HTMLSession()
page = html.get("https://joanribot.github.io/Proyecto/")
page_text = page.text


def get_next_target(page_text):
    start_link = page_text.find("<a href")
    if start_link == -1:
        return None, 0
    start_quote = page_text.find('=', start_link)
    end_quote = page_text.find('>', start_quote + 1)
    url = page_text[start_quote + 1 : end_quote]
    return url, end_quote

def all_links(page_text):
    lista = []
    while True:
        url, endpos = get_next_target(page_text)
        if url:
            lista.append(url)
            page_text = page_text[endpos:]
        else:
            break
    assert lista == ['https://joanribot.github.io/Proyecto/Menus/china.html', 'https://joanribot.github.io/Proyecto/Menus/spain.html', 'https://joanribot.github.io/Proyecto/Menus/tailandesa.html', 'https://joanribot.github.io/Proyecto/Menus/mexicana.html', 'https://joanribot.github.io/Proyecto/Menus/italiana.html', 'https://joanribot.github.io/Proyecto/Menus/francesa.html']
    return lista

urls = all_links(page_text)

def entra_aqui(urls):
    html_links = []
    for link in urls:
        hola = HTMLSession()
        link = hola.get(link)
        link_text = link.text
        html_links.append(link_text)
    return html_links

htmls = entra_aqui(urls)

<<<<<<< HEAD
def buscaAtributos(htmlPais, atributo):
    buscar = htmlPais.find(atributo)
    if buscar==-1:
        return None,0
    desde = htmlPais.find('>', buscar)         
    hasta = htmlPais.find('<', desde)               
    encontrado = htmlPais[desde + 1 : hasta]
    htmlPais=htmlPais[hasta:] 
    return encontrado,htmlPais

def menuCompleto(Atributos,html):
    diccionario={}
    resto=""
    for i in Atributos:
        nombre, resto= buscaAtributos(html,i)
        if nombre==None:
            return None, 0
        diccionario[i]=nombre
    return diccionario, resto

def menusCompletos(html,Atributos):
    resto=html
    count=0
    menusPagina={}
    while True:
        diccionario, resto=menuCompleto(Atributos,resto)
        if diccionario ==None:
            break
        menusPagina[count]=diccionario
        count+=1
    return menusPagina


def BuscaMenu(htmls):
    Atributos = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]
    paises=["China", "España", "Tailandia", "Mexico", "Italia","Francia"]
    count=0
    jason={}
    for i in htmls:
        menus=menusCompletos(i,Atributos)
        jason[paises[count]]=menus
        count+=1
    return jason
            
print(BuscaMenu(htmls))
=======
#def vamos_a_probar(htmls):
    #diccionario = {}
    #numero_menu = 0
    #while True:
        #json, hasta = find_menu(htmls)
        #numero_menu += 1
        #if json:
            #diccionario[numero_menu] = json
            #json = {}
            #htmls = htmls[hasta:]
    #return diccionario

def entra_en_cada_pais(htmls):
    diccionario = {}
    for pais in htmls:
        if pais:
            find_menu(pais)
        else:
            return diccionario

def find_menu(pais):
    paises = ["China", "España,", "Tailandia", "Mexico", "Italia", "Francia"]
    diccionario_json = {}
    json_prueba = {}
    numero_menu = 1
    while True:
        json, hasta = vuelve_info(pais)
        if json:
            diccionario_json[numero_menu] = json
            for nombre_menu_pais in paises:              
                json_prueba[nombre_menu_pais] = diccionario_json
                if len(json_prueba) != 6:
                    numero_menu += 1
                    pais = pais[hasta:]
                    json, hasta = vuelve_info(pais)
                    diccionario_json[numero_menu] = json
                    json_prueba[nombre_menu_pais] = diccionario_json
                    if len(json_prueba) != 6:
                        numero_menu += 1
                        pais = pais[hasta:]
                        json, hasta = vuelve_info(pais)
                        diccionario_json[numero_menu] = json
                        json_prueba[nombre_menu_pais] = diccionario_json
                        if len(json_prueba) != 6:
                            numero_menu += 1
                            pais = pais[hasta:]
                            json, hasta = vuelve_info(pais)
                            diccionario_json[numero_menu] = json
                            json_prueba[nombre_menu_pais] = diccionario_json
                else:
                    return json_prueba
        else:
            return json_prueba
    return json_prueba


def vuelve_info(pais):
    info = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]
    json = {}
    numero_de_veces_recorrido = 1
    for nombre in info:
        if numero_de_veces_recorrido <= 8:    
            nombre_menu = pais.find(nombre)             
            if nombre_menu == -1:                       
                return None, 0
            desde = pais.find('>', nombre_menu)         
            hasta = pais.find('<', desde)               
            menu = pais[desde + 1 : hasta]
            json[nombre] = menu
            numero_de_veces_recorrido += 1
        else:
            return json, hasta + 1
    return json, hasta + 1


print(entra_en_cada_pais(htmls))
>>>>>>> 4a967913fc8987cb48ebc0e339d072d0f8693f79
