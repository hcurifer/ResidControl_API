from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def crear_usuario(db: Session, usuario: UsuarioCreate):
    hash_contra = get_password_hash(usuario.contrasenia)
    db_usuario = Usuario(
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        email=usuario.email,
        contrasenia_hash=hash_contra,
        rol=usuario.rol,
        numero_empresa=usuario.numero_empresa
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()
    
def obtener_usuario_por_id(db: Session, id_usuario: int):
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

def obtener_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def obtener_usuario_por_numero_empresa(db: Session, numero_empresa: str):
    return db.query(Usuario).filter(Usuario.numero_empresa == numero_empresa).first()

