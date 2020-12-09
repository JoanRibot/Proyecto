import pymongo
from .programa import json

try:
    uri = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.8i6ry.mongodb.net/test"
    client = pymongo.MongoClient(uri)
    client.server_info()
    print ("Conectado al servidor")
except pymongo.errors.ServerSelectionTimeoutError as error:
    print( "Error al conectar al servidor") % error
except pymongo.errors.CollectionInvalid as error:
    print("could not connect to MongoDB") % error

db = client.proyecto
collection = db.diccionario
collection.drop()

try:    
    collection.insert_one(json)
    print("Successfully added")
except Exception as error:
    print("Error saving data")

