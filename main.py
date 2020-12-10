from services.src.extraer_atributos_html  import sube_colecciones, Atributos
from services.src.html_string import htmls
from services.src.conexion_bd import borrar_coleccion

sube_colecciones(htmls,Atributos) #subir los diccionarios a la coleccion de la Base de Datos


#borrar_coleccion() ##borrar la coleccion de la Base de Datos
