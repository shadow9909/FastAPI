from blog import models
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


from datetime import datetime, timedelta
from jose import JWTError, jwt

from .token import create_access_token

router = APIRouter(
    tags=['Authentication']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Passwords")

    access_token = create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
