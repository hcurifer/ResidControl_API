from sqlalchemy.orm import Session
from app.models.alarma import Alarma
from app.schemas.alarma import AlarmaCreate
from typing import List
from datetime import datetime
from sqlalchemy import func  

# Crear una nueva alarma
def crear_alarma(db: Session, alarma: AlarmaCreate):
    db_alarma = Alarma(**alarma.dict())
    db.add(db_alarma)
    db.commit()
    db.refresh(db_alarma)
    return db_alarma

# Obtener todas las alarmas
def obtener_alarmas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Alarma).offset(skip).limit(limit).all()

# Obtener una alarma por ID
def obtener_alarma_por_id(db: Session, id_alarma: int):
    return db.query(Alarma).filter(Alarma.id_alarma == id_alarma).first()

# Cambiar el estado de una alarma
def cambiar_estado_alarma(db: Session, id_alarma: int, nuevo_estado: str):
    alarma = db.query(Alarma).filter(Alarma.id_alarma == id_alarma).first()
    if not alarma:
        return None
    alarma.estado = nuevo_estado
    db.commit()
    db.refresh(alarma)
    return alarma

# Obtener alarmas por estado (pendiente o completada)
def obtener_alarmas_por_estado(db: Session, estado: str):
    return db.query(Alarma).filter(Alarma.estado == estado).all()

# Obtener alarmas pendientes por fecha
def obtener_alarmas_pendientes_por_fecha(db: Session, fecha: str):
    return db.query(Alarma).filter(
        Alarma.estado == "pendiente",
        func.date(Alarma.fecha) == fecha
    ).all()
