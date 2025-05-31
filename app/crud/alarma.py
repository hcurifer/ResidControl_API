from sqlalchemy.orm import Session
from app.models.alarma import Alarma
from app.schemas.alarma import AlarmaCreate
from typing import List
from datetime import datetime, date
from sqlalchemy import func  
from sqlalchemy.orm import joinedload
from app.models.usuario import Usuario
from app.models.residente import Residente
from app.schemas.alarma import AlarmaConNombres

# Crear una nueva alarma
def crear_alarma(db: Session, alarma: AlarmaCreate):
    db_alarma = Alarma(**alarma.dict())
    db.add(db_alarma)
    db.commit()
    db.refresh(db_alarma)
    return db_alarma

# Obtener todas las alarmas
def obtener_alarmas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Alarma).offset(skip).limit(limit).all()

# Obtener una alarma por ID
def obtener_alarma_por_id(db: Session, id_alarma: int):
    return db.query(Alarma).filter(Alarma.id_alarma == id_alarma).first()

# Cambiar el estado de una alarma
def cambiar_estado_alarma(db: Session, id_alarma: int, nuevo_estado: str):
    alarma = db.query(Alarma).filter(Alarma.id_alarma == id_alarma).first()
    if not alarma:
        return None
    alarma.estado = nuevo_estado
    db.commit()
    db.refresh(alarma)
    return alarma

# Obtener alarmas por estado (pendiente o completada)
def obtener_alarmas_por_estado(db: Session, estado: str):
    return db.query(Alarma).filter(Alarma.estado == estado).all()

# Obtener alarmas pendientes por fecha
def obtener_alarmas_pendientes_por_fecha(db: Session, fecha: str):
    return db.query(Alarma).filter(
        Alarma.estado == "pendiente",
        func.date(Alarma.fecha) == fecha
    ).all()
# Obtener alarmas por estado (pendiente o completada) pero con NOMBRE haciendo join a otras tablas
def obtener_alarmas_con_nombres(db: Session, estado: str):
    alarmas = db.query(Alarma).filter(Alarma.estado == estado).all()

    resultado = []
    for alarma in alarmas:
        enfermero = db.query(Usuario).filter(Usuario.id_usuario == alarma.id_usuario).first()
        residente = db.query(Residente).filter(Residente.id_residente == alarma.id_residente).first()
        
        resultado.append(AlarmaConNombres(
            id_alarma=alarma.id_alarma,
            descripcion=alarma.descripcion,
            estado=alarma.estado,
            fecha=alarma.fecha,
            enfermero=f"{enfermero.nombre} {enfermero.apellidos}" if enfermero else None,
            residente=f"{residente.nombre} {residente.apellidos}" if residente else None,
        ))

    return resultado

# Obtener alarmas filtrando por fecha indicada 

def obtener_alarmas_por_estado_y_fecha_con_nombres(db: Session, estado: str, fecha: date):
    alarmas = db.query(Alarma).filter(
        Alarma.estado == estado,
        func.date(Alarma.fecha) == fecha
    ).all()

    resultado = []
    for alarma in alarmas:
        enfermero = db.query(Usuario).filter(Usuario.id_usuario == alarma.id_usuario).first()
        residente = db.query(Residente).filter(Residente.id_residente == alarma.id_residente).first()
        
        resultado.append(AlarmaConNombres(
            id_alarma=alarma.id_alarma,
            descripcion=alarma.descripcion,
            estado=alarma.estado,
            fecha=alarma.fecha,
            enfermero=f"{enfermero.nombre} {enfermero.apellidos}" if enfermero else None,
            residente=f"{residente.nombre} {residente.apellidos}" if residente else None,
        ))

    return resultado
