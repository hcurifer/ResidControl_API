from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db.base import Base

class Turno(Base):
    __tablename__ = "turnos"

    id_turno = Column(Integer, primary_key=True, index=True)
    tipo_turno = Column(String(20), nullable=False)
    fecha = Column(Date, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="SET NULL"))
