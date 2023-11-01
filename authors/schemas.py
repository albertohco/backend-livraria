from pydantic import BaseModel


class AuthorBase(BaseModel):
    nome: str
    email: str
    telefone: str

class AuthorCreate(AuthorBase):...

class Author(AuthorBase):
    id: int

    class ConfigDict:
        from_attributes = True


class AuthorList(BaseModel):
    items: list[Author]