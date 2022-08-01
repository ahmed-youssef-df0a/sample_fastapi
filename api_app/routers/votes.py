from .. import crud, schemas , oauth2
from ..database import  get_db
from fastapi import   status , HTTPException , Depends , APIRouter
from sqlalchemy.orm import Session 


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/")
async def create_vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return crud.create_vote(db=db, vote=vote , current_user=current_user)
