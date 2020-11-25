from src.findAtributes import findMenu, findPlato1, findPlato2, findPlato3, findPrice, findStock, findValoration

def test_findMenu():
    assert findMenu('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')== 'Menú Dragón'

def test_findPlato1():
    assert findPlato1('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')=='Dos rollitos de primavera'

def test_findPlato2():
    assert findPlato2('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')=="Ternera en salsa de otras"

def test_findPlato3():
    assert findPlato3('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')=="Helado frito"

def test_findStock():
    assert findPrice('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')=="12,95€"

def test_findPrice():
    assert findStock('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')=="53u"

def test_findValoration():
    assert findValoration('<td class="quitar"><ul class="menus"><li><h3 class="menuCompleto">Menú Dragón</h3></li><li class="plato1">Dos rollitos de primavera</li><li class="plato2">Ternera en salsa de otras</li><li class="plato3">Helado frito</li><li class="plato4">Refresco o agua</li></ul><nav><table class="tablamenus2" border="2" align="center"><tr><td>STOCK</td><td class="stck">53u</td></tr><tr><td>PRECIO</td><td class="price">12,95€</td></tr><tr><td>VALORACIÓN</td><td class="valoration">4,2⭐</td></tr></table></nav>')==('4,2⭐','</td></tr></table></nav>')