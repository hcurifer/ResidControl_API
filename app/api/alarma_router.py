from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.alarma import AlarmaCreate, AlarmaOut
from app.db.session import SessionLocal
from app.crud.alarma import (
    crear_alarma,
    obtener_alarmas,
    obtener_alarma_por_id,
    cambiar_estado_alarma,
    obtener_alarmas_por_estado
    obtener_alarmas_pendientes_por_fecha
)

router = APIRouter(
    prefix="/alarmas",
    tags=["Alarmas"]
)

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear nueva alarma
@router.post("/", response_model=AlarmaOut)
def crear(alarma: AlarmaCreate, db: Session = Depends(get_db)):
    return crear_alarma(db, alarma)

# Listar todas las alarmas
@router.get("/", response_model=List[AlarmaOut])
def listar(db: Session = Depends(get_db)):
    return obtener_alarmas(db)

# Obtener alarma por ID
@router.get("/{id_alarma}", response_model=AlarmaOut)
def obtener(id_alarma: int, db: Session = Depends(get_db)):
    alarma = obtener_alarma_por_id(db, id_alarma)
    if not alarma:
        raise HTTPException(status_code=404, detail="Alarma no encontrada")
    return alarma

# Cambiar estado de una alarma
@router.put("/{id_alarma}/estado", response_model=AlarmaOut)
def actualizar_estado(id_alarma: int, nuevo_estado: str, db: Session = Depends(get_db)):
    alarma = cambiar_estado_alarma(db, id_alarma, nuevo_estado)
    if not alarma:
        raise HTTPException(status_code=404, detail="Alarma no encontrada")
    return alarma

# Filtrar alarmas por estado
@router.get("/estado/{estado}", response_model=List[AlarmaOut])
def filtrar_por_estado(estado: str, db: Session = Depends(get_db)):
    return obtener_alarmas_por_estado(db, estado)

# Filtrar alarmas pendientes por fecha
@router.get("/pendientes/fecha/{fecha}", response_model=List[AlarmaOut])
def pendientes_por_fecha(fecha: str, db: Session = Depends(get_db)):
    return obtener_alarmas_pendientes_por_fecha(db, fecha)