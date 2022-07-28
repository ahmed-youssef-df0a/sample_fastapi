import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String , DateTime, text

from .database import Base

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP , nullable=False, server_default=text('now()'))



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP , nullable=False, server_default=text('now()'))
