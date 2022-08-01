
from typing import Optional
from fastapi import HTTPException, Response , status
from sqlalchemy.orm import Session

from . import models, schemas
from .utils import get_password_hash, verify_password






# Post
def get_post(db: Session, post_id: int):
    return db.query(models.Posts).filter(models.Posts.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100, search : Optional[str] = ""):
    posts=db.query(models.Posts).filter(models.Posts.title.contains(search)).order_by(models.Posts.created_at.asc()).offset(skip).limit(limit).all()
    return posts

def create_post(db: Session, post: schemas.PostBase , current_user : int):
    the_post = models.Posts(**post.dict() , user_id=current_user)
    db.add(the_post)
    db.commit()
    db.refresh(the_post)
    return the_post


def delete_post(db: Session, post_id: int ,current_user : int):
    the_post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if the_post :
        if the_post.user_id == current_user:
            db.delete(the_post)
            db.commit()
            return True
        else:
            raise  HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorithed for this action")

    return False

def update_post(db: Session, post_id: int, post: schemas.PostBase ,current_user : int):
    the_post = db.query(models.Posts).filter(models.Posts.id == post_id).first()
    if the_post :
        if the_post.user_id == current_user:
            the_post.title = post.title
            the_post.content = post.content
            the_post.published = post.published
            db.commit()
            db.refresh(the_post)
            return the_post
        else:
            raise  HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorithed for this action")
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

def check_user(db: Session, user_credentials : schemas.UserLogin):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if user and verify_password(user_credentials.password, user.password):
        return user
    return None


def create_vote(db: Session, vote: schemas.Vote , current_user : int):
    #check if post_id exists
    the_post = db.query(models.Posts).filter(models.Posts.id == vote.post_id).first() 
    if the_post :
        the_vote = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user)
        
        
        if vote.dir == 1:
            if the_vote.first() :
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="You already voted for this post")
            new_vote = models.Vote(post_id=vote.post_id, user_id=current_user)
            db.add(new_vote)
            db.commit()
            db.refresh(new_vote)
            return { "message" : "Vote created" , "vote" : new_vote } 
        else:
            if not the_vote.first() :
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You haven't voted for this post")
            else:
                the_vote.delete(synchronize_session=False)
                db.commit()
                return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

