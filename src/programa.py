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

def find_menu(htmls):
    info = ["menuCompleto", "plato1", "plato2", "plato3", "plato4", "stck", "price", "valoration"]
    diccionario = {}
    numero_menu = 0
    for pais in htmls:
        json = {}
        numero_menu += 1
        for nombre in info:
            nombre_menu = pais.find(nombre)             
            if nombre_menu == -1:                       
                return menu, hasta
            desde = pais.find('>', nombre_menu)         
            hasta = pais.find('<', desde)               
            menu = pais[desde + 1 : hasta]              
            json[nombre] = menu
        diccionario[numero_menu] = json  
    return diccionario                    

print(find_menu(htmls))