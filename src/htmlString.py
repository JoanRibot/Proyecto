from requests_html import HTMLSession

html = HTMLSession()
page = html.get("https://joanribot.github.io/Proyecto/")
page_text = page.text


def get_next_target(page_text):

    # Precondición
    assert isinstance(page_text, str)

    start_link = page_text.find("<a href")
    if start_link == -1:
        return None, 0
    start_quote = page_text.find('=', start_link)
    end_quote = page_text.find('>', start_quote + 1)
    url = page_text[start_quote + 1 : end_quote]

    assert isinstance(url, str)
    assert isinstance(end_quote, int)

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

    # Postcondición 
    assert lista == ['https://joanribot.github.io/Proyecto/Menus/china.html', 'https://joanribot.github.io/Proyecto/Menus/spain.html', 'https://joanribot.github.io/Proyecto/Menus/tailandesa.html', 'https://joanribot.github.io/Proyecto/Menus/mexicana.html', 'https://joanribot.github.io/Proyecto/Menus/italiana.html', 'https://joanribot.github.io/Proyecto/Menus/francesa.html']
    return lista

urls = all_links(page_text)

def htmlTodo(urls):
    html_links = []
    for link in urls:
        link = HTMLSession().get(link)
        link_text = link.text
        html_links.append(link_text)
    return html_links

htmls = htmlTodo(urls)

