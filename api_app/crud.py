
from sqlalchemy.orm import Session

from . import models, schemas
from .utils import get_password_hash






# Post
def get_post(db: Session, post_id: int):
    return db.query(models.Posts).filter(models.Posts.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    posts=db.query(models.Posts).offset(skip).limit(limit).all()
    return posts

def create_post(db: Session, post: schemas.PostBase):
    the_post = models.Posts(**post.dict())
    db.add(the_post)
    db.commit()
    db.refresh(the_post)
    return the_post


def delete_post(db: Session, post_id: int):
    the_post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if the_post:
        db.delete(the_post)
        db.commit()
        return True
    return False

def update_post(db: Session, post_id: int, post: schemas.PostBase):
    the_post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if the_post:
        the_post.title = post.title
        the_post.content = post.content
        the_post.published = post.published
        db.commit()
        db.refresh(the_post)
        return the_post
    return None

# User
def create_user(db: Session, user: schemas.UserBase):
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    the_user = models.User(**user.dict())
    db.add(the_user)
    db.commit()
    db.refresh(the_user)
    return the_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
