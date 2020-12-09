from requests_html import HTMLSession
<<<<<<< HEAD
=======

>>>>>>> 13efe837b44800e7ccd2c09ffb3bd0f2a28117d1
def made_text(principal_link):
    assert isinstance(principal_link,str)
    try:
        html = HTMLSession()
        page = html.get(principal_link)
        page_html = page.text
        return page_html
    except:
        print("No se pudo obtener el html")

