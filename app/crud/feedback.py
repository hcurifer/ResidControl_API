from sqlalchemy.orm import Session
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate
from typing import List

# Crear nuevo registro de feedback
def crear_feedback(db: Session, feedback: FeedbackCreate):
    db_feedback = Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

# Obtener todos los feedbacks (ordenados por fecha descendente)
def obtener_feedback(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Feedback).order_by(Feedback.fecha.desc()).offset(skip).limit(limit).all()
