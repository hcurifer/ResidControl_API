from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.db.base import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id_feedback = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha = Column(DateTime, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario", ondelete="SET NULL"))
