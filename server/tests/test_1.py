from service import get_secret, generate
from sequrety import encrypt, decrypt
from config.mongo_client import db_connect
from bson import ObjectId


def test_1():
    """ тестируем модуль шифрования """
    secret = "hello world"
    password = "12345678"
    hash = encrypt(secret, password)
    result = decrypt(hash, password)
    assert secret == result


def test_2():
    """ тестируем модуль генерации секретов """
    secret = "hello world"
    password = "12345678"
    url = generate(secret, password)
    object_id = url["secret url"].split("/")[4]
    db = db_connect()
    collection = db.get_collection("secret")
    my_data = collection.find_one({"_id": ObjectId(object_id)})
    assert my_data is not None


def test_3():
    """ тестируем модуль получения секретов """
    secret = "hello world"
    password = "12345678"
    url = generate(secret, password)
    object_id = url["secret url"].split("/")[4]
    result = get_secret(object_id, password)
    assert result["result"] == secret
