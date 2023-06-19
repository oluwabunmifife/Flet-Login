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

@router.post("/register", status_code=201)
async def new_user(user: module.UserCreate, request:Request, db: Session = Depends(get_db)):
    checker = db.query(models.User).filter(models.User.username == user.username).first()
    if checker:
        raise HTTPException(status_code=400, detail="Username already exists")
    new =  crud.create_user(user=user, db=db)
    result = await request.body()
    # print(result)
    return {
        "userId": new.id,
        "username": new.username
    }