from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.residente import ResidenteCreate, ResidenteOut
from app.db.session import SessionLocal
from app.crud.residente import (
    crear_residente,
    obtener_residentes,
    obtener_residente_por_id,
    buscar_residente_por_nombre_apellidos,
    actualizar_estado_residente,  
    eliminar_residente 
)

router = APIRouter(
    prefix="/residentes",
    tags=["Residentes"]
)

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear residente
@router.post("/", response_model=ResidenteOut)
def crear(residente: ResidenteCreate, db: Session = Depends(get_db)):
    return crear_residente(db, residente)

# Listar residentes
@router.get("/", response_model=List[ResidenteOut])
def listar(db: Session = Depends(get_db)):
    return obtener_residentes(db)

# Buscar por ID
@router.get("/{id_residente}", response_model=ResidenteOut)
def obtener(id_residente: int, db: Session = Depends(get_db)):
    residente = obtener_residente_por_id(db, id_residente)
    if not residente:
        raise HTTPException(status_code=404, detail="Residente no encontrado")
    return residente

# Buscar por nombre y apellidos
@router.get("/buscar/", response_model=List[ResidenteOut])
def buscar(
    nombre: str = Query(..., description="Nombre del residente"),
    apellidos: str = Query(..., description="Apellidos del residente"),
    db: Session = Depends(get_db)
):
    resultados = buscar_residente_por_nombre_apellidos(db, nombre, apellidos)
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron residentes")
    return resultados

@router.put("/{id_residente}/estado", response_model=ResidenteOut)
def actualizar_estado(id_residente: int, nuevo_estado: str, db: Session = Depends(get_db)):
    residente = actualizar_estado_residente(db, id_residente, nuevo_estado)
    if not residente:
        raise HTTPException(status_code=404, detail="Residente no encontrado")
    return residente

@router.delete("/{id_residente}", status_code=204)
def eliminar(id_residente: int, db: Session = Depends(get_db)):
    exito = eliminar_residente(db, id_residente)
    if not exito:
        raise HTTPException(status_code=404, detail="Residente no encontrado")
