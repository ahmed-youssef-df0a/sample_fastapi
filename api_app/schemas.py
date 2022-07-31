from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional




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



class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    user_id: int

    class Config:
        orm_mode = True


# Post

class PostBase(BaseModel):
    title: str
    content: str
    published : bool = True


    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    id: Optional[int] = None
    user_id: int

class PostInDB(PostBase,PostCreate):
    created_at: datetime
    user_owner : UserResponse

    class Config:
        orm_mode = True

