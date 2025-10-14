from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel


Base = declarative_base()


# SQLAlchemy modelleri
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)


# Pydantic modelleri
class UserCreate(BaseModel):
    name: str
    email: str
    age: int


class UserUpdate(BaseModel):
    name: str = None
    email: str = None
    age: int = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    
    class Config:
        from_attributes = True


