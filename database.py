import certifi
from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://umb_api:12345@api.cwxdash.mongodb.net/'

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
