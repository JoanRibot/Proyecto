from requests_html import HTMLSession

def made_text(principal_link):
    assert isinstance(principal_link,str)
    try:
        html = HTMLSession()
        page = html.get(principal_link)
        page_html = page.text
        return page_html
    except:
        print("No se pudo obtener el html")

