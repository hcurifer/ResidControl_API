from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.db.session import SessionLocal
from app.crud.usuario import crear_usuario, obtener_usuarios, obtener_usuario_por_id, obtener_usuario_por_email

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UsuarioOut)
def crear(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = obtener_usuario_por_email(db, usuario.email)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return crear_usuario(db, usuario)

@router.get("/", response_model=List[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return obtener_usuarios(db)

@router.get("/{id_usuario}", response_model=UsuarioOut)
def obtener_por_id(id_usuario: int, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_id(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
