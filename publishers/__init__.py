from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.utils import verify_token
from database import get_db
from publishers import crud, schemas

router = APIRouter(prefix="/editoras", tags=["editoras"], dependencies=[Depends(verify_token)])

@router.post("", response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    db_publisher = crud.create_publisher(db, publisher)
    return db_publisher

@router.get("", response_model=schemas.PublisherList)
def get_publishers(db: Session = Depends(get_db)):
    publishers = crud.get_publishers(db)
    return {"items": publishers}