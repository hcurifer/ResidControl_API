from sqlalchemy.orm import Session
from app.models.turno import Turno
from app.schemas.turno import TurnoCreate

# Crear un nuevo turno
def crear_turno(db: Session, turno: TurnoCreate):
    db_turno = Turno(**turno.dict())
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

# Obtener todos los turnos
def obtener_turnos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Turno).offset(skip).limit(limit).all()

# Obtener turnos por fecha
def obtener_turnos_por_fecha(db: Session, fecha: str):
    return db.query(Turno).filter(Turno.fecha == fecha).all()

# Obtener turno por ID
def obtener_turno_por_id(db: Session, id_turno: int):
    return db.query(Turno).filter(Turno.id_turno == id_turno).first()
