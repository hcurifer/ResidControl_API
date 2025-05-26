from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Tarea(Base):
    __tablename__ = "tareas"

    id_tarea = Column(Integer, primary_key=True, index=True)
    descripcion = Column(Text, nullable=False)
    estado = Column(String(20), nullable=False)
    fecha = Column(Date, nullable=False)
    duracion_minutos = Column(Integer, nullable=False, default=30)

    id_enfermero = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="SET NULL"))
    id_turno = Column(Integer, ForeignKey("turnos.id_turno", ondelete="SET NULL"))

    # Relaciones opcionales para ORM (si decides usarlas más adelante)
    enfermero = relationship("Usuario", backref="tareas", lazy="joined")
    turno = relationship("Turno", backref="tareas", lazy="joined")
