from pydantic import BaseModel
from pydantic.fields import Field

from authors.schemas import Author
from categories.schemas import Category
from publishers.schemas import Publisher


class BookBase(BaseModel):
    titulo: str
    isbn: str
    paginas: int
    ano: int
    capa: str

class BookCreate(BookBase):
    category_id: int = Field(alias="categoriaId")
    publisher_id: int = Field(alias="editoraId")
    author_id: int = Field(alias="autorId")

class Book(BookBase):
    id: int
    codigo: str
    categoria: Category
    editora: Publisher
    autor: Author

    class ConfigDict:
        from_attributes = True

class BookList(BaseModel):
    items: list[Book]
