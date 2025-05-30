from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.db.session import SessionLocal
from app.models.usuario import Usuario
from app.crud.usuario import (
    crear_usuario,
    obtener_usuarios,
    obtener_usuario_por_id,
    obtener_usuario_por_email,
    obtener_usuario_por_numero_empresa
)
from passlib.context import CryptContext
from app.schemas.usuario import UsuarioLogin

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

# Seguridad para contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear usuario
@router.post("/", response_model=UsuarioOut)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar que no exista el email
    if db.query(Usuario).filter_by(email=usuario.email).first():
        raise HTTPException(status_code=400, detail="Email ya registrado")

    hashed_password = pwd_context.hash(usuario.contrasenia)

    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        edad=usuario.edad,
        email=usuario.email,
        contrasenia_hash=hashed_password,
        rol=usuario.rol,
        numero_empresa=usuario.numero_empresa
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

# Obtener lista de usuarios
@router.get("/", response_model=List[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return obtener_usuarios(db)

# Obtener usuario por ID
@router.get("/{id_usuario}", response_model=UsuarioOut)
def obtener_por_id(id_usuario: int, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_id(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


# Login por número de empresa y contraseña
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    numero_empresa = datos.numero_empresa
    contrasenia = datos.contrasenia

    usuario = obtener_usuario_por_numero_empresa(db, numero_empresa)

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if not pwd_context.verify(contrasenia, usuario.contrasenia_hash):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    return {
        "mensaje": "Login correcto",
        "usuario": UsuarioOut.model_validate(usuario),  # devuelve objeto validado
        "token": "fake-jwt"
    }
