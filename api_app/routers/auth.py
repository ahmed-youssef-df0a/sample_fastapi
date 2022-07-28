from fastapi import APIRouter, Depends, HTTPException , status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import Token
from ..crud import check_user
from ..oauth2 import create_access_token, get_current_user


router = APIRouter(
    prefix="/login",
    tags=["Authntication"]
)

@router.post("/", response_model=Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db) ):
    
    user = check_user(db=db, user_credentials=user_credentials)
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    access_token = create_access_token(data = { "user_id" : user.id })
    return Token(access_token=access_token)