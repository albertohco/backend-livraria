from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import Session

from auth import schemas
from database import models


def get_user_by_email(db: Session, email:str):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    return db_user

def create_user(db: Session, user: schemas.User):
    hashed_password = pbkdf2_sha256.hash(user.senha)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user