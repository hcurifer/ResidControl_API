from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Residente(Base):
    __tablename__ = "residentes"

    id_residente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    estado = Column(String(20), nullable=False)
    habitacion = Column(String(10), nullable=False)
    ubicacion = Column(String(100), nullable=True)
    fecha_ingreso = Column(Date, nullable=True)
