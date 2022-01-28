from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))

    creator = relationship("User", back_populates="blog")


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blog = relationship("Blog", back_populates="creator")
