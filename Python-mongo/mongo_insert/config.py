from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "Usuarios"

def get_database():
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]
