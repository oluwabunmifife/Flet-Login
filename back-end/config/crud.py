from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models
from schemas import module

def get_user(db: Session, username: str):
    user_info = db.query(models.User).filter(models.User.username == username).first()

    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info

def get_wallets(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(user: module.UserCreate, db: Session):
    db_user = models.User(username=user.username, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(user: module.UserLogin, db: Session):
    # user_info = db.query(models.User).filter(models.User.username == user.username).first()
    user_info = get_user(db, user.username)
    user_password = user.password

    get_password = db.query(models.User).filter(models.User.hashed_password == user_password).first()

    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    elif get_password is None:
        raise HTTPException(status_code=401, detail="Invalid password")
    return user_info
