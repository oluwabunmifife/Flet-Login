#FastAPI imports
from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

#Submodules
from config import crud
from config import models
from schemas import module
from config.db import SessionLocal, engine
#from main import get_db

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/login", status_code=200)
async def login(user: module.UserLogin, request: Request, db: Session = Depends(get_db)):
    user_login = crud.login_user(user=user, db=db)
    result = await request.body()
    # print(result)
    # print(type(result))

    return {
        "username": user_login.username
    }