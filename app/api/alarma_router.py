from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, date
from app.schemas.alarma import AlarmaCreate, AlarmaOut, AlarmaConNombres
from app.db.session import SessionLocal
from app.crud.alarma import (
    crear_alarma,
    obtener_alarmas,
    obtener_alarma_por_id,
    cambiar_estado_alarma,
    obtener_alarmas_por_estado,
    obtener_alarmas_pendientes_por_fecha,
    obtener_alarmas_con_nombres,
    obtener_alarmas_por_estado_y_fecha_con_nombres
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

# Filtar alarmas por fecha 
@router.get("/filtrar", response_model=List[AlarmaConNombres])
def filtrar_alarmas(
    estado: str = Query(...),
    fecha: str = Query(...),  # <- ahora recibimos como str
    db: Session = Depends(get_db)
):
    try:
        fecha_convertida = datetime.strptime(fecha, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha inválido. Usa YYYY-MM-DD.")
    
    return obtener_alarmas_por_estado_y_fecha_con_nombres(db, estado, fecha_convertida)


# Filtrar alarmas por estado
@router.get("/estado/{estado}", response_model=List[AlarmaOut])
def filtrar_por_estado(estado: str, db: Session = Depends(get_db)):
    return obtener_alarmas_por_estado(db, estado)

# Filtrar alarmas por estado y Nombres
@router.get("/estado/{estado}/con-nombres", response_model=List[AlarmaConNombres])
def filtrar_con_nombres(estado: str, db: Session = Depends(get_db)):
    return obtener_alarmas_con_nombres(db, estado)

# Filtrar alarmas pendientes por fecha
@router.get("/pendientes/fecha/{fecha}", response_model=List[AlarmaOut])
def pendientes_por_fecha(fecha: str, db: Session = Depends(get_db)):
    return obtener_alarmas_pendientes_por_fecha(db, fecha)

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


# Eliminar alarmas por id
@router.delete("/{id_alarma}", status_code=204)
def eliminar_alarma(id_alarma: int, db: Session = Depends(get_db)):
    alarma = obtener_alarma_por_id(db, id_alarma)
    if not alarma:
        raise HTTPException(status_code=404, detail="Alarma no encontrada")

    db.delete(alarma)
    db.commit()

