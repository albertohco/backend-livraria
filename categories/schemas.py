from pydantic import BaseModel


class CategoryBase(BaseModel):
    nome: str


class CategoryCreate(CategoryBase):...

class Category(CategoryBase):
    id: int

    class ConfigDict:
        from_attributes = True

class CategoryList(BaseModel):
    items: list[Category]