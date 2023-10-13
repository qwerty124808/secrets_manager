from config.mongo_client import db_connect
from sequrety import encrypt, decrypt
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId


def generate(secret, password):
    secret_key = encrypt(secret, password)

    db = db_connect()

    collection = db.get_collection("secret")
    collection.create_index("created_at", expireAfterSeconds=900)
    new_secret = collection.insert_one({"hash": secret_key, "created_at": datetime.utcnow()})
    if new_secret.acknowledged:
        object_id = new_secret.inserted_id
        return {"secret url": f"http://127.0.0.1:8000/secret/{object_id}"}
    return {"message": "error occured while creating secret"}


def get_secret(secret_key, password):
    db = db_connect()
    collection = db.get_collection("secret")
    try:
        my_data = collection.find_one({"_id": ObjectId(secret_key)})
        if my_data is None:
            return {"message": "ошибка, данные не найдены"}
        result = my_data.get("hash")
        print(result)
        decrypted = decrypt(result, password)
        my_data = collection.delete_many({"_id": ObjectId(secret_key)})
        return {"result": decrypted}
    except (UnicodeDecodeError, InvalidId):
        return {"message": "ошибка расшифровки, неверные данные"}
