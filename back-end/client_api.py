from fastapi import FastAPI
from routes import register, login
from config.db import engine, SessionLocal
from config import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(register.router)
app.include_router(login.router)