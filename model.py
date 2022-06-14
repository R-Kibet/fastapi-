from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class bg(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("Users.id"))

    creator = relationship("User", back_populates="blog")


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    Tel = Column(Integer)

    blog = relationship("bg", back_populates="creator")
