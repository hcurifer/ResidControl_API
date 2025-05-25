from sqlalchemy.orm import Session
from app.models.residente import Residente
from app.schemas.residente import ResidenteCreate

# Crear un nuevo residente
def crear_residente(db: Session, residente: ResidenteCreate):
    db_residente = Residente(**residente.dict())
    db.add(db_residente)
    db.commit()
    db.refresh(db_residente)
    return db_residente

# Obtener todos los residentes
def obtener_residentes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Residente).offset(skip).limit(limit).all()

# Obtener un residente por su ID
def obtener_residente_por_id(db: Session, id_residente: int):
    return db.query(Residente).filter(Residente.id_residente == id_residente).first()

def buscar_residente_por_nombre_apellidos(db: Session, nombre: str, apellidos: str):
    return db.query(Residente).filter(
        Residente.nombre.ilike(f"%{nombre}%"),
        Residente.apellidos.ilike(f"%{apellidos}%")
    ).all()

def actualizar_estado_residente(db: Session, id_residente: int, nuevo_estado: str):
    residente = db.query(Residente).filter(Residente.id_residente == id_residente).first()
    if not residente:
        return None
    residente.estado = nuevo_estado
    db.commit()
    db.refresh(residente)
    return residente

def eliminar_residente(db: Session, id_residente: int):
    residente = db.query(Residente).filter(Residente.id_residente == id_residente).first()
    if not residente:
        return False
    db.delete(residente)
    db.commit()
    return True

