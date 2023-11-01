from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import crud, schemas, utils
from database import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/signup")
def signup(credentials: schemas.UserCreate, db:Session = Depends(get_db)):
    if not credentials.senha == credentials.confirmarSenha:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Senhas devem ser iguais") 

    user = crud.create_user(db, credentials)
    token = utils.create_token(credentials, db)
    
    return token


@router.post("/login")
def login(token=Depends(utils.create_token)):
    return token