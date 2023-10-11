from fastapi import FastAPI, Request
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html
import service
from models.shemas import Secret, GetSecret



app = FastAPI()

@app.get("/docs")
async def read_docs():
    """FastAPI-swagger"""
    return get_swagger_ui_html(openapi_url="/openapi.json")


@app.post("/generate")
async def generate(data: Secret):
    """
        принимает secret, password
        Return: secret url
    """
    
    secret = data.secret
    password = data.password
    return service.generate(secret, password)


@app.post("/secret/{secret_key}")
async def secret(secret_key: str, data: GetSecret):
    """ 
        Возвращает секрет.\n
        Принимает:- secret_key: str - id секрета, password\n
        Возвращает - данные конкретного секрета.
    """
    password = data.password
    return service.get_secret(secret_key, password)
        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
