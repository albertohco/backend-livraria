from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True)
    hashed_password = Column(String)

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    isbn = Column(String)
    paginas = Column(Integer)
    codigo = Column(String)
    ano = Column(Integer)
    capa = Column(String)

    publisher_id = Column(Integer, ForeignKey("publisher.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    author_id = Column(Integer, ForeignKey("author.id"))

    editora = relationship("Publisher", back_populates="books")
    categoria = relationship("Category", back_populates="books")
    autor = relationship("Author", back_populates="books")


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)

    books = relationship("Book", back_populates="editora")

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)

    books = relationship("Book", back_populates="categoria")


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)

    books = relationship("Book", back_populates="autor")

