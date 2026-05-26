from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()
# 🛠️ LINHA 7 ALTERADA: Adicionamos o "or" com o caminho padrão caso o .env falhe
DATABASE_URL = os.getenv("DATABASE_URL") or "sqlite:///./sql_app.db"

engine =  create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass 

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()