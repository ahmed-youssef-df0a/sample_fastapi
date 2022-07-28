from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional


# Post

class PostBase(BaseModel):
    title: str
    content: str
    published : bool = True


    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    id: Optional[int] = None




class PostInDB(PostBase,PostCreate):
    created_at: datetime

    class Config:
        orm_mode = True



# User

class UserBase(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
