from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.notificacion import NotificacionCreate, NotificacionOut
from app.db.session import SessionLocal
from app.crud.notificacion import (
    crear_notificacion,
    obtener_notificaciones,
    obtener_notificaciones_por_alarma
)

router = APIRouter(
    prefix="/notificaciones",
    tags=["Notificaciones"]
)

# Dependencia para sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear nueva notificación
@router.post("/", response_model=NotificacionOut)
def crear(notificacion: NotificacionCreate, db: Session = Depends(get_db)):
    return crear_notificacion(db, notificacion)

# Obtener historial de notificaciones
@router.get("/", response_model=List[NotificacionOut])
def listar(db: Session = Depends(get_db)):
    return obtener_notificaciones(db)

# Obtener notificaciones por alarma
@router.get("/por-alarma/{id_alarma}", response_model=List[NotificacionOut])
def por_alarma(id_alarma: int, db: Session = Depends(get_db)):
    return obtener_notificaciones_por_alarma(db, id_alarma)
