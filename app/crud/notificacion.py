from sqlalchemy.orm import Session
from app.models.notificacion import Notificacion
from app.schemas.notificacion import NotificacionCreate
from typing import List

# Crear nueva notificación
def crear_notificacion(db: Session, notificacion: NotificacionCreate):
    db_notificacion = Notificacion(**notificacion.dict())
    db.add(db_notificacion)
    db.commit()
    db.refresh(db_notificacion)
    return db_notificacion

# Obtener todas las notificaciones (historial)
def obtener_notificaciones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notificacion).order_by(Notificacion.fecha_envio.desc()).offset(skip).limit(limit).all()

# Obtener notificaciones por id de alarma
def obtener_notificaciones_por_alarma(db: Session, id_alarma: int):
    return db.query(Notificacion).filter(Notificacion.id_alarma == id_alarma).order_by(Notificacion.fecha_envio.desc()).all()
