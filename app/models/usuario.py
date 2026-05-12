from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, index=True, unique=True)
    senha_hash = Column(String(255), nullable=False)

    role = Column(String(20), nullable=False, default="usuario")

    ativo = Column(Boolean, default=True)

    criado_em = Column(DateTime, server_default=func.now())