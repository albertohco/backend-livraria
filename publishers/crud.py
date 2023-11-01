from sqlalchemy.orm import Session

from database import models
from publishers import schemas


def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = models.Publisher(**publisher.model_dump())
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_publishers(db: Session):
    publisher = db.query(models.Publisher).all()
    return publisher