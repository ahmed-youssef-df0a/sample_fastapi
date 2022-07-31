import datetime
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String , ForeignKey, text
from sqlalchemy.orm import relationship

from .database import Base

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False,  server_default=text('True'))
    created_at = Column(TIMESTAMP , nullable=False, server_default=text('now()'))
    user_id =  Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user_owner =  relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP , nullable=False, server_default=text('now()'))
    

