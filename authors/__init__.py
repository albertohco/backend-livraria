from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.utils import verify_token
from authors import crud, schemas
from database import get_db

router = APIRouter(prefix="/autores", tags=["autores"], dependencies=[Depends(verify_token)])

@router.post("", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = crud.create_author(db, author)
    return db_author

@router.get("", response_model=schemas.AuthorList)
def get_authors(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    return {"items": authors}
