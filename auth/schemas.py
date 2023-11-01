from pydantic import BaseModel


class User(BaseModel):
    email: str
    senha: str


class UserCreate(User):
    confirmarSenha:str