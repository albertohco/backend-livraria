from pydantic import BaseModel


class PublisherBase(BaseModel):
    nome: str
    endereco: str
    telefone: str

class PublisherCreate(PublisherBase):...

class Publisher(PublisherBase):
    id: int
    
    class ConfigDict:
        from_attributes = True

class PublisherList(BaseModel):
    items: list[Publisher]
