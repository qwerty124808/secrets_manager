from fastapi import FastAPI, Request
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html
import service



app = FastAPI()

@app.get("/docs")
async def read_docs():
    """FastAPI-swagger"""
    return get_swagger_ui_html(openapi_url="/openapi.json")


@app.post("/generate")
async def generate(data: Request):
    """
        принимает secret, password
        Return: secret url
    """
    data = await data.json()
    secret = data["secret"]
    password = data["password"]
    return service.generate(secret, password)


@app.post("/secret/{secret_key}")
async def secret(secret_key: str, data: Request):
    """ 
        Возвращает секрет.
        Принимает:- secret_key: str - id секрета
        Возвращает - данные конкретного секрета.
    """
    data = await data.json()
    password = data["password"]
    return service.get_secret(secret_key, password)
        

if __name__ == "__main__":
    uvicorn.run(app)
