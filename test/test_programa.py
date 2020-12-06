from src.programa import buscaAtributos, menuCompleto, menusCompletos
from .htmlDePrueba import  tipoMedicamento, htmlMedicamentosPequeño, htmlMedicamentosGrande

import pytest

@pytest.mark.buscaAtributos
def test_buscaAtributos():
    assert buscaAtributos("<body><p class='tiempo'>hace sol</p></body>", "tiempo")== ("hace sol","</p></body>")
    assert buscaAtributos("<body><p class='tiemp'>hace sol</p>", "tiempo")== (None,0)
    assert buscaAtributos("<body><h1 class='verde'>lechuga</h1></body><p class='verde'>arbol</p></body>", "verde")== ("lechuga","</h1></body><p class='verde'>arbol</p></body>")
    assert buscaAtributos("<body><h2 class='medicamentos'>Ramipril</h2><h5 class='MEDICAMENTOS'>Escitaloplam</h5></body>", "MEDICAMENTOS")== ("Escitaloplam","</h5></body>")
    assert buscaAtributos("<body><p class='Marvel'>IceMan</p></body>", "marvel")== (None,0)
    
@pytest.mark.menuCompleto
def test_menuCompleto():
    assert menuCompleto(tipoMedicamento,htmlMedicamentosPequeño)==({"AINE":"Ibuprofeno","Diuretico":"Furosemida","Antihipertensivo":"Ramipril","Benzodiazepina":"Diazepam","Hipolipemiante":"Simvastatina","Antidepresivo":"Fluoxetina"},"</p></html>")
    assert menuCompleto(["noExiste","AINE", "Diuretico"],htmlMedicamentosPequeño)==(None,0)
    assert menuCompleto(tipoMedicamento,htmlMedicamentosGrande)==({"AINE":"Dexketoprofeno","Diuretico":"Torasemida","Antihipertensivo":"Enalapril","Benzodiazepina":"Lorazepam","Hipolipemiante":"Atorvastatina","Antidepresivo":"Duloxetina"},'</p></h1><h2><p class="AINE">Ibuprofeno</p><p class="Diuretico">Furosemida</p><p class="Antihipertensivo">Ramipril</p><p class="Benzodiazepina">Diazepam</p><p class="Hipolipemiante">Simvastatina</p><p class="Antidepresivo">Fluoxetina</p></h2><h3><p class="AINE">Naproxeno</p><p class="Diuretico">Indapamida</p><p class="Antihipertensivo">Lisinopril</p><p class="Benzodiazepina">Alprazolam</p><p class="Hipolipemiante">Rosuvastatina</p><p class="Antidepresivo">Escitalopram</p></h2></h3></html>')

@pytest.mark.menusCompletos
def test_menusCompletod():
    assert menusCompletos(htmlMedicamentosPequeño,tipoMedicamento)=={0:{"AINE":"Ibuprofeno","Diuretico":"Furosemida","Antihipertensivo":"Ramipril","Benzodiazepina":"Diazepam","Hipolipemiante":"Simvastatina","Antidepresivo":"Fluoxetina"}}
    assert menusCompletos(htmlMedicamentosGrande,tipoMedicamento)=={0:{"AINE":"Dexketoprofeno","Diuretico":"Torasemida","Antihipertensivo":"Enalapril","Benzodiazepina":"Lorazepam","Hipolipemiante":"Atorvastatina","Antidepresivo":"Duloxetina"},1:{"AINE":"Ibuprofeno","Diuretico":"Furosemida","Antihipertensivo":"Ramipril","Benzodiazepina":"Diazepam","Hipolipemiante":"Simvastatina","Antidepresivo":"Fluoxetina"},2:{"AINE":"Naproxeno","Diuretico":"Indapamida","Antihipertensivo":"Lisinopril","Benzodiazepina":"Alprazolam","Hipolipemiante":"Rosuvastatina","Antidepresivo":"Escitalopram"}}
    assert menusCompletos(htmlMedicamentosGrande,["nada","Aine","Antihipertensivo"])=={}