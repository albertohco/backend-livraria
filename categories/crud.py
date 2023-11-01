from sqlalchemy.orm import Session

from categories import schemas
from database import models


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    categories = db.query(models.Category).all()
    return categories