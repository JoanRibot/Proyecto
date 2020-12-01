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
    assert urls == ['https://joanribot.github.io/Proyecto/Menus/china.html', 'https://joanribot.github.io/Proyecto/Menus/spain.html', 'https://joanribot.github.io/Proyecto/Menus/tailandesa.html', 'https://joanribot.github.io/Proyecto/Menus/mexicana.html', 'https://joanribot.github.io/Proyecto/Menus/italiana.html', 'https://joanribot.github.io/Proyecto/Menus/francesa.html']
    html_links = []
    for link in urls:
        hola = HTMLSession()
        link = hola.get(link)
        link_text = link.text
        html_links.append(link_text)
    return html_links

htmls = entra_aqui(urls)

#def entra_en_cada_pais(htmls):
    #for pais in htmls:
        #return pais

def find_menu(htmls):
    paises = ["China", "España,", "Tailandia", "Mexico", "Italia", "Francia"]
    diccionario_json = {}
    json_prueba = {}
    numero_menu = 0
    numero_pais = 0
    
    for nombre_menu_pais in paises:
        numero_menu = 0
        pais = htmls[numero_pais]
        cuenta_cuantos = pais
        numero_pais += 1
        if nombre_menu_pais in json_prueba:
            break
        while len(json_prueba) <= 6:
            numero_menu += 1
            json, hasta = vuelve_info(pais)
            diccionario_json[numero_menu] = json
            json_prueba[nombre_menu_pais] = diccionario_json
            if len(json_prueba[nombre_menu_pais]) == cuenta_cuantos.count("valoration"):
                break
            pais = pais[hasta:]
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
            break
    return json, hasta


print(find_menu(htmls))