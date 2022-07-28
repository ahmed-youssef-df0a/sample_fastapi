from fastapi import APIRouter, Depends, HTTPException , status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserLogin, UserResponse
from ..crud import check_user


router = APIRouter(
    prefix="/login",
    tags=["Authntication"]
)

@router.post("/", response_model=UserResponse)
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = check_user(db=db, user_credentials=user_credentials)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user