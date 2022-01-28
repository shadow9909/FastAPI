from ..database import get_db
from .. import models
from fastapi import Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id ==
                                 id).delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(
        models.Blog.id == id).one_or_none()
    if not blog:
        return Response(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found")

    for var, value in vars(request).items():
        setattr(blog, var, value) if value else None

    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def get_with_id(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=404, detail=f"Blog with ID {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with ID {id} not found"}
    return blog
