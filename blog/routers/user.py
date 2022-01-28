from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from passlib.context import CryptContext
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['User']
)
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # new_user = models.User(
    #     name=request.name, email=request.email, password=pwd_context.hash(request.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser, tags=['User'])
def get_user(id: int, db: Session = Depends(get_db)):
    # user = db.query(models.User).filter(models.User.id == id).one_or_none()
    # if not user:
    #     return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")

    # return user
    return user.get(id, db)
