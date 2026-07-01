from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
