from .descarga_html import made_text

principal_link = "https://joanribot.github.io/Proyecto"


def get_next_target(page_text): 

    assert isinstance(page_text, str)
    
    url = ""
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
    assert isinstance(page_text, str)
    lista = []
    while True:
        url, endpos = get_next_target(page_text)
        if url:
            lista.append(url)
            page_text = page_text[endpos:]
        else:
            break

    assert isinstance(lista, list) 
    return lista

def html_todas_paginas(urls):
    assert isinstance(urls, list) 

    html_links = []
    for link in urls:
        link_text = made_text(link)
        html_links.append(link_text)

    assert isinstance(html_links, list)  
    return html_links


def crawl_web(seed):
    assert isinstance(seed, str)

    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            for i in all_links(made_text(page)):
                if i not in tocrawl:
                    tocrawl.append(i)
            crawled.append(page)

    assert isinstance(crawled, list) 
    return crawled


links = crawl_web(principal_link)
htmls = html_todas_paginas(links)
