from .. import crud, schemas , oauth2
from ..database import  get_db
from typing import List, Optional
from fastapi import  Response , status , HTTPException , Depends , APIRouter
from sqlalchemy.orm import Session 


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/" , response_model=List[schemas.PostInDB])
async def get_posts(skip: int = 0, db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user),
                    limit : int = 10,
                    search : Optional[str] = ""
                    ):
    
    posts = crud.get_posts(db, skip=skip, limit=limit, search=search)

    return  posts


@router.get("/{post_id}", response_model=schemas.PostInDB)
async def get_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = crud.get_post(db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.post("/", response_model=schemas.PostInDB , status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return crud.create_post(db=db, post=post,current_user=current_user)


@router.delete("/{post_id}")
async def delete_post(post_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    deleted_post = crud.delete_post(db=db, post_id=post_id,current_user=current_user)
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{post_id}", response_model=schemas.PostInDB) 
async def update_post(post_id: int, post: schemas.PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    updated_post = crud.update_post(db=db, post_id=post_id, post=post ,current_user=current_user)
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return updated_post
