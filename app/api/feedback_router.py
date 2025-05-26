from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.feedback import FeedbackCreate, FeedbackOut
from app.db.session import SessionLocal
from app.crud.feedback import crear_feedback, obtener_feedback

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

# Dependencia para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear nuevo feedback
@router.post("/", response_model=FeedbackOut)
def crear(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    return crear_feedback(db, feedback)

# Listar feedbacks (historial)
@router.get("/", response_model=List[FeedbackOut])
def listar(db: Session = Depends(get_db)):
    return obtener_feedback(db)
