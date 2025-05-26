from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.turno import TurnoCreate, TurnoOut
from app.db.session import SessionLocal
from app.crud.turno import (
    crear_turno,
    obtener_turnos,
    obtener_turnos_por_fecha,
    obtener_turno_por_id
)

router = APIRouter(
    prefix="/turnos",
    tags=["Turnos"]
)

# Obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear un nuevo turno
@router.post("/", response_model=TurnoOut)
def crear(turno: TurnoCreate, db: Session = Depends(get_db)):
    return crear_turno(db, turno)

# Obtener todos los turnos
@router.get("/", response_model=List[TurnoOut])
def listar(db: Session = Depends(get_db)):
    return obtener_turnos(db)

# Obtener turnos por fecha
@router.get("/por-fecha/{fecha}", response_model=List[TurnoOut])
def por_fecha(fecha: str, db: Session = Depends(get_db)):
    turnos = obtener_turnos_por_fecha(db, fecha)
    if not turnos:
        raise HTTPException(status_code=404, detail="No hay turnos para esa fecha")
    return turnos

# Obtener turno por ID
@router.get("/{id_turno}", response_model=TurnoOut)
def obtener(id_turno: int, db: Session = Depends(get_db)):
    turno = obtener_turno_por_id(db, id_turno)
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno
