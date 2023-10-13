from pydantic import BaseModel


class Secret(BaseModel):
    secret: str
    password: str


class GetSecret(BaseModel):
    password: str
