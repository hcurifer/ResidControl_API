from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Notificacion(Base):
    __tablename__ = "notificaciones"

    id_notificacion = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha_envio = Column(DateTime, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="SET NULL"))
    id_residente = Column(Integer, ForeignKey("residentes.id_residente", ondelete="SET NULL"))
    id_alarma = Column(Integer, ForeignKey("alarmas.id_alarma", ondelete="SET NULL"))

    # Relaciones
    usuario = relationship("Usuario")
    residente = relationship("Residente")
    alarma = relationship("Alarma")
