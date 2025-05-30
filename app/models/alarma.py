from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from app.db.base import Base

class Alarma(Base):
    __tablename__ = "alarmas"

    id_alarma = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    descripcion = Column(Text, nullable=False)
    estado = Column(String(20), nullable=False)
    fecha = Column(DateTime, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="SET NULL"))
    id_residente = Column(Integer, ForeignKey("residentes.id_residente", ondelete="SET NULL"))
