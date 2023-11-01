from sqlalchemy.orm import Session

from authors import schemas
from database import models


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_authors(db: Session):
    authors = db.query(models.Author).all()
    return authors
