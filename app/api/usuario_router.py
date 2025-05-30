from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.usuario import UsuarioCreate, UsuarioOut
from app.db.session import SessionLocal
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
def crear(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = obtener_usuario_por_email(db, usuario.email)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return crear_usuario(db, usuario)

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
# Login por número de empresa y contraseña
@router.post("/login")
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    numero_empresa = datos.numero_empresa
    contrasenia = datos.contrasenia

    print("🔐 Intentando login...")
    print("📨 Número recibido:", numero_empresa)
    print("📨 Contraseña recibida:", contrasenia)

    usuario = obtener_usuario_por_numero_empresa(db, numero_empresa)

    if not usuario:
        print("❌ Usuario no encontrado")
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    print("✅ Usuario encontrado en DB:", usuario.numero_empresa)
    print("🔒 Hash en DB:", usuario.contrasenia_hash)

    es_valida = pwd_context.verify(contrasenia, usuario.contrasenia_hash)
    print("🔎 ¿Contraseña válida?:", es_valida)

    if not es_valida:
        print("❌ Contraseña incorrecta")
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    print("✅ Login exitoso")

    return {
        "mensaje": "Login correcto",
        "usuario": {
            "id": usuario.id_usuario,
            "nombre": usuario.nombre,
            "apellidos": usuario.apellidos,
            "email": usuario.email,
            "rol": usuario.rol,
            "numero_empresa": usuario.numero_empresa
        },
        "token": "fake-jwt"
    }
