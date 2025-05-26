from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from app.schemas.tarea import TareaCreate, TareaOut
from app.db.session import SessionLocal
from app.crud.tarea import (
    crear_tarea,
    obtener_tareas,
    obtener_tarea_por_id,
    cambiar_estado_tarea,
    obtener_tareas_por_filtro
)

router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

# Obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear nueva tarea
@router.post("/", response_model=TareaOut)
def crear(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crear_tarea(db, tarea)

# Obtener todas las tareas
@router.get("/", response_model=List[TareaOut])
def listar(db: Session = Depends(get_db)):
    return obtener_tareas(db)

# Obtener tarea por ID
@router.get("/{id_tarea}", response_model=TareaOut)
def obtener(id_tarea: int, db: Session = Depends(get_db)):
    tarea = obtener_tarea_por_id(db, id_tarea)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

# Cambiar estado de la tarea
@router.put("/{id_tarea}/estado", response_model=TareaOut)
def cambiar_estado(id_tarea: int, nuevo_estado: str, db: Session = Depends(get_db)):
    tarea = cambiar_estado_tarea(db, id_tarea, nuevo_estado)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

# Filtrar tareas por enfermero, fecha, turno y estado
@router.get("/filtrar", response_model=List[TareaOut])
def filtrar_tareas(
    id_enfermero: int,
    fecha: date,
    id_turno: int,
    estado: str = Query(..., regex="^(pendiente|completada)$"),
    db: Session = Depends(get_db)
):
    return obtener_tareas_por_filtro(db, id_enfermero, fecha, id_turno, estado)
