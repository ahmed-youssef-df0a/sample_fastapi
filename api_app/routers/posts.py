from .. import crud, schemas 
from ..database import  get_db
from typing import List
from fastapi import  Response , status , HTTPException , Depends , APIRouter
from sqlalchemy.orm import Session 


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/" , response_model=List[schemas.PostInDB])
async def get_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)

    return  posts


@router.get("/{post_id}", response_model=schemas.PostInDB)
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.post("/", response_model=schemas.PostInDB , status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.PostBase, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


@router.delete("/{post_id}")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = crud.delete_post(db=db, post_id=post_id)
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{post_id}", response_model=schemas.PostInDB) 
async def update_post(post_id: int, post: schemas.PostBase, db: Session = Depends(get_db)):
    updated_post = crud.update_post(db=db, post_id=post_id, post=post)
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return updated_post