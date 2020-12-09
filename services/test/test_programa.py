from services.src.programa import busca_atributo, menu_completo, menus_completos, busca_menu
from .htmlDePrueba import  tipoMedicamento, htmlMedicamentosPequeño, htmlMedicamentosGrande, htmlsAnimales,page_prueba


import pytest

@pytest.mark.busca_atributo
def test_busca_atributo():
    assert busca_atributo("<body><p class='tiempo'>hace sol</p></body>", "tiempo") == ("hace sol","</p></body>")
    assert busca_atributo("<body><p class='tiemp'>hace sol</p>", "tiempo") == (None,0)
    assert busca_atributo("<body><h1 class='verde'>lechuga</h1></body><p class='verde'>arbol</p></body>", "verde") == ("lechuga","</h1></body><p class='verde'>arbol</p></body>")
    assert busca_atributo("<body><h2 class='medicamentos'>Ramipril</h2><h5 class='MEDICAMENTOS'>Escitaloplam</h5></body>", "MEDICAMENTOS") == ("Escitaloplam","</h5></body>")
    assert busca_atributo("<body><p class='Marvel'>IceMan</p></body>", "marvel") == (None,0)
    
@pytest.mark.menu_completo
def test_menu_completo():
    assert menu_completo(tipoMedicamento,htmlMedicamentosPequeño) == ({"AINE":"Ibuprofeno","Diuretico":"Furosemida","Antihipertensivo":"Ramipril","Benzodiazepina":"Diazepam","Hipolipemiante":"Simvastatina","Antidepresivo":"Fluoxetina"},"</p></html>")
    assert menu_completo(["noExiste","AINE", "Diuretico"],htmlMedicamentosPequeño) == (None,0)
    assert menu_completo(tipoMedicamento,htmlMedicamentosGrande) == ({"AINE":"Dexketoprofeno","Diuretico":"Torasemida","Antihipertensivo":"Enalapril","Benzodiazepina":"Lorazepam","Hipolipemiante":"Atorvastatina","Antidepresivo":"Duloxetina"},'</p></h1><h2><p class="AINE">Ibuprofeno</p><p class="Diuretico">Furosemida</p><p class="Antihipertensivo">Ramipril</p><p class="Benzodiazepina">Diazepam</p><p class="Hipolipemiante">Simvastatina</p><p class="Antidepresivo">Fluoxetina</p></h2><h3><p class="AINE">Naproxeno</p><p class="Diuretico">Indapamida</p><p class="Antihipertensivo">Lisinopril</p><p class="Benzodiazepina">Alprazolam</p><p class="Hipolipemiante">Rosuvastatina</p><p class="Antidepresivo">Escitalopram</p></h2></h3></html>')

@pytest.mark.menus_completos
def test_menus_completos():
    assert menus_completos(htmlMedicamentosPequeño,tipoMedicamento) == {"menu1":{"AINE":"Ibuprofeno","Diuretico":"Furosemida","Antihipertensivo":"Ramipril","Benzodiazepina":"Diazepam","Hipolipemiante":"Simvastatina","Antidepresivo":"Fluoxetina"}}
    assert menus_completos(htmlMedicamentosGrande,tipoMedicamento) == {"menu1":{"AINE":"Dexketoprofeno","Diuretico":"Torasemida","Antihipertensivo":"Enalapril","Benzodiazepina":"Lorazepam","Hipolipemiante":"Atorvastatina","Antidepresivo":"Duloxetina"},"menu2":{"AINE":"Ibuprofeno","Diuretico":"Furosemida","Antihipertensivo":"Ramipril","Benzodiazepina":"Diazepam","Hipolipemiante":"Simvastatina","Antidepresivo":"Fluoxetina"},"menu3":{"AINE":"Naproxeno","Diuretico":"Indapamida","Antihipertensivo":"Lisinopril","Benzodiazepina":"Alprazolam","Hipolipemiante":"Rosuvastatina","Antidepresivo":"Escitalopram"}}
    assert menus_completos(htmlMedicamentosGrande,["nada","Aine","Antihipertensivo"]) == {}
    assert menus_completos('<p class="mamifero">mapache</p>< class="ave>loro</p>',tipoMedicamento) == {}

@pytest.mark.busca_menu
def test_busca_menus():
    assert busca_menu(htmlsAnimales,["primero","segundo","tercero"])=={"mamifero":{"menu1":{"primero":"Mono","segundo":"Rata","tercero":"ornitorrinco"},"menu2":{"primero":"Ardilla","segundo":"Ratón","tercero":"Cabra"}},"ave":{"menu1":{"primero":"Loro","segundo":"Avestruz","tercero":"Gallina"},"menu2":{"primero":"Gaviota","segundo":"Paloma","tercero":"Colibrí"}},"Bicho":{"menu1":{"primero":"hormiga","segundo":"mosquito","tercero":"escarabajo"},"menu2":{"primero":"dragonfly","segundo":"mosca","tercero":"abeja"}}}

