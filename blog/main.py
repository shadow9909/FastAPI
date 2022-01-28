from typing import List
from sqlalchemy.orm.session import Session
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models, database
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .database import get_db
import blog
from .routers import blog, user, authentication

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['Blog'])
# def create(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=2)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.delete('/blog/{id}', status_code=204, tags=['Blog'])
# def destroy(id, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id ==
#                                  id).delete(synchronize_session=False)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put('/blog/{id}', status_code=200, tags=['Blog'])
# def put(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(
#         models.Blog.id == id).one_or_none()
#     if not blog:
#         return Response(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found")

#     for var, value in vars(request).items():
#         setattr(blog, var, value) if value else None

#     db.add(blog)
#     db.commit()
#     db.refresh(blog)
#     return blog


# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['Blog'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blog'])
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(
#             status_code=404, detail=f"Blog with ID {id} not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f"Blog with ID {id} not found"}
#     return blog


# @app.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED, tags=['User'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(
#         name=request.name, email=request.email, password=pwd_context.hash(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['User'])
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).one_or_none()
#     if not user:
#         return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with {id} not found")

#     return user
