from ..database import get_db
from .. import models
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name, email=request.email, password=pwd_context.hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).one_or_none()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")

    return user
