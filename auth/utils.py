import time
from datetime import datetime, timedelta
from http import HTTPStatus

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import Session

from auth import crud, schemas
from database import get_db

SECRET = "secret"
ALGORITHM = "HS256"

bearer = HTTPBearer()

def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if not user:
        return

    if not pbkdf2_sha256.verify(password, user.hashed_password):
        return

    return user

def create_token(credentials: schemas.User, db = Depends(get_db)):
    user = authenticate_user(db, credentials.email, credentials.senha)
    if not user:
        raise HTTPException(HTTPStatus.UNAUTHORIZED, "Email ou senha inválidos")
    
    expiration_date = datetime.utcnow() + timedelta(minutes=15)
    token = jwt.encode({'email': credentials.email, "exp": expiration_date}, SECRET, ALGORITHM)
    unix_time = time.mktime(expiration_date.timetuple())

    return {
        "token": token,
        "exp": unix_time
    }

def verify_token(token: HTTPAuthorizationCredentials =  Depends(bearer), db: Session = Depends(get_db)):
    try:
        data = jwt.decode(token.credentials, SECRET, algorithms=ALGORITHM)
    except jwt.exceptions.DecodeError:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Token inválido")
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Token expirado")
    
    email = data.get("email")
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(HTTPStatus.UNAUTHORIZED, "Credencial inválida")

    return data