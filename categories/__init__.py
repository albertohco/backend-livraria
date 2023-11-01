from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.utils import verify_token
from categories import crud, schemas
from database import get_db

router = APIRouter(prefix="/categorias", tags=["categorias"], dependencies=[Depends(verify_token)])

@router.post("", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.create_category(db, category)
    return db_category

@router.get("", response_model=schemas.CategoryList)
def get_categories(db: Session = Depends(get_db)):
    categories = crud.get_categories(db)
    return {"items": categories}