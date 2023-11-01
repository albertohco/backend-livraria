from sqlalchemy.orm import Session

from books import schemas
from database import models


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db_book.codigo = str(id(db_book))
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, q: str = "", limit: int = 100):
    books = db.query(models.Book)
    """
    select * from book
    """

    if q:
        books = books.filter(models.Book.titulo.icontains(q))
        """
        select * from book
        where titulo like '%q%'
        """
    
    books = books.limit(limit).all()
    return books

def get_book(db: Session, livro_id: int):
    book = db.query(models.Book).filter(models.Book.id == livro_id).first()
    return book

def delete_book(db: Session, livro_id: int):
    db_book = get_book(db, livro_id)
    if not db_book:
        return
    
    db.delete(db_book)
    db.commit()
    return db_book

def update_book(db: Session, livro_id: int, book: schemas.BookCreate):
    db_book = get_book(db, livro_id)
    if not db_book:
        return
    
    db_book.titulo = book.titulo
    db_book.isbn = book.isbn
    db_book.paginas = book.paginas
    db_book.ano = book.ano
    db_book.capa = book.capa
    db_book.publisher_id = book.publisher_id
    db_book.author_id = book.author_id
    db_book.category_id = book.category_id

    db.add(db_book)
    db.commit()
    return db_book