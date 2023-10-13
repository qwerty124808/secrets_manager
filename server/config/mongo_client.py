from pymongo import MongoClient
import os


def db_connect():
    client = MongoClient(os.getenv("DB_URL"))
    db_name = os.getenv("DB_NAME")
    db = client.get_database(db_name)
    return db