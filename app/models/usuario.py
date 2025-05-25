from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    contrasenia_hash = Column(Text, nullable=False)
    rol = Column(String(20), nullable=False)
