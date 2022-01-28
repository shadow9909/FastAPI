from blog.routers.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog
from .oauth2 import get_current_user

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)


@router.get('/', response_model=List[schemas.ShowBlog], tags=['Blog'])
def all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(get_current_user)):
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, tags=['Blog'])
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    # new_blog = models.Blog(title=request.title, body=request.body, user_id=2)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request, db)


@router.delete('/{id}', status_code=204, tags=['Blog'])
def destroy(id: int, db: Session = Depends(get_db)):
    # db.query(models.Blog).filter(models.Blog.id ==
    #                              id).delete(synchronize_session=False)
    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    return blog.delete(id, db)


@router.put('/{id}', status_code=200, tags=['Blog'])
def put(id, request: schemas.Blog, db: Session = Depends(get_db)):
    # blog = db.query(models.Blog).filter(
    #     models.Blog.id == id).one_or_none()
    # if not blog:
    #     return Response(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found")

    # for var, value in vars(request).items():
    #     setattr(blog, var, value) if value else None

    # db.add(blog)
    # db.commit()
    # db.refresh(blog)
    # return blog
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blog'])
def show(id, db: Session = Depends(get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(
    #         status_code=404, detail=f"Blog with ID {id} not found")
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {'detail': f"Blog with ID {id} not found"}
    # return blog
    return blog.get_with_id(id, db)
