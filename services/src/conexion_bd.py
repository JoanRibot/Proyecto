import pymongo

def subir_json_bd(json):
    try:
        uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wiedk.mongodb.net/test"
        client = pymongo.MongoClient(uri)
        client.server_info()
        print ("Conectado al servidor")
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print( "Error al conectar al servidor") % error
    except pymongo.errors.CollectionInvalid as error:
        print("No se pudo conectar a MongoCompass") % error

    db = client.proyecto
    collection = db.diccionario

    try:    
        collection.insert_one(json)
        print("Añadido correctamente")
    except Exception as error:
        print("Hubo un error al añadir el archivo")

def borrar_coleccion():
    try:
        uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.wiedk.mongodb.net/test"
        client = pymongo.MongoClient(uri)
        client.server_info()
        print ("Conectado al servidor")
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print( "Error al conectar al servidor") % error
    except pymongo.errors.CollectionInvalid as error:
        print("No se pudo conectar a MongoCompass") % error

    db = client.proyecto
    collection = db.diccionario

    try:
        collection.drop()
        print("La coleccion se ha borrado correctamente")
    except pymongo.errors.ServerSelectionTimeoutError as error:
        print( "Error al conectar al servidor") % error
    except pymongo.errors.CollectionInvalid as error:
        print("No se pudo conectar a MongoCompass") % error
    
