from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.notificacion import NotificacionCreate, NotificacionOut
from app.db.session import SessionLocal
from app.crud.notificacion import (
    crear_notificacion,
    obtener_notificaciones,
    obtener_notificaciones_por_alarma,
    obtener_notificaciones_con_nombres,
)

router = APIRouter(
    prefix="/notificaciones",
    tags=["Notificaciones"]
)

# Dependencia para sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear nueva notificación
@router.post("/", response_model=NotificacionOut)
def crear(notificacion: NotificacionCreate, db: Session = Depends(get_db)):
    return crear_notificacion(db, notificacion)

# Obtener historial de notificaciones
@router.get("/", response_model=List[NotificacionOut])
def listar(db: Session = Depends(get_db)):
    return obtener_notificaciones(db)

# Obtener notificaciones por alarma
@router.get("/por-alarma/{id_alarma}", response_model=List[NotificacionOut])
def por_alarma(id_alarma: int, db: Session = Depends(get_db)):
    return obtener_notificaciones_por_alarma(db, id_alarma)


@router.get("/con-nombres")
def listar_con_nombres(db: Session = Depends(get_db)):
    notificaciones = obtener_notificaciones_con_nombres(db)
    return [
        {
            "tipo": n.tipo,
            "contenido": n.contenido,
            "fecha_envio": n.fecha_envio,
            "usuario": f"{n.usuario.nombre} {n.usuario.apellidos}" if n.usuario else "Desconocido",
            "residente": f"{n.residente.nombre} {n.residente.apellidos}" if n.residente else "Desconocido",
            "alarma": n.alarma.descripcion if n.alarma else "Desconocida"
        }
        for n in notificaciones
    ]



@router.get("/con-nombres")
def listar_con_nombres(db: Session = Depends(get_db)):
    notificaciones = db.query(Notificacion)\
        .options(
            joinedload(Notificacion.usuario),
            joinedload(Notificacion.residente),
            joinedload(Notificacion.alarma)
        )\
        .order_by(Notificacion.id_notificacion.desc())\
        .limit(5)\
        .all()

    return [
        {
            "tipo": n.tipo,
            "contenido": n.contenido,
            "fecha_envio": n.fecha_envio,
            "usuario": f"{n.usuario.nombre} {n.usuario.apellidos}" if n.usuario else "Desconocido",
            "residente": f"{n.residente.nombre} {n.residente.apellidos}" if n.residente else "Desconocido",
            "alarma": n.alarma.descripcion if n.alarma else "Desconocida"
        }
        for n in notificaciones
    ]

@router.get("/ultimas")
def ultimas_notificaciones(db: Session = Depends(get_db)):
    notificaciones = db.query(Notificacion).order_by(Notificacion.id_notificacion.desc()).limit(5).all()
    return notificaciones

@router.get("/con-nombres")
def listar_con_nombres(db: Session = Depends(get_db)):
    notificaciones = db.query(Notificacion)\
        .options(
            joinedload(Notificacion.usuario, innerjoin=False),
            joinedload(Notificacion.residente, innerjoin=False),
            joinedload(Notificacion.alarma, innerjoin=False)
        )\
        .order_by(Notificacion.id_notificacion.desc())\
        .limit(5)\
        .all()

    return [
        {
            "tipo": n.tipo,
            "contenido": n.contenido,
            "fecha_envio": n.fecha_envio,
            "usuario": f"{n.usuario.nombre} {n.usuario.apellidos}" if n.usuario else "Desconocido",
            "residente": f"{n.residente.nombre} {n.residente.apellidos}" if n.residente else "Desconocido",
            "alarma": n.alarma.descripcion if n.alarma else "Desconocida"
        }
        for n in notificaciones
    ]
