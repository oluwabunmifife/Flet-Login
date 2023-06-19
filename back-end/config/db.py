from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root@localhost:3306/fletapp"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
meta = MetaData()

conn = engine.connect()
Base = declarative_base()