from sqlalchemy.orm import Session
from app.models.tarea import Tarea
from app.schemas.tarea import TareaCreate
from datetime import date
from typing import Optional



# Crear una nueva tarea
def crear_tarea(db: Session, tarea: TareaCreate):
    db_tarea = Tarea(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

# Obtener todas las tareas
def obtener_tareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tarea).offset(skip).limit(limit).all()

# Obtener una tarea por ID
def obtener_tarea_por_id(db: Session, id_tarea: int):
    return db.query(Tarea).filter(Tarea.id_tarea == id_tarea).first()

# Cambiar el estado de una tarea
def cambiar_estado_tarea(db: Session, id_tarea: int, nuevo_estado: str):
    tarea = db.query(Tarea).filter(Tarea.id_tarea == id_tarea).first()
    if not tarea:
        return None
    tarea.estado = nuevo_estado
    db.commit()
    db.refresh(tarea)
    return tarea

def obtener_tareas_por_filtro(
    db: Session,
    id_usuario: int,
    fecha: date,
    estado: str,
    id_turno: Optional[int] = None  
):
    query = db.query(Tarea).filter(
        Tarea.id_usuario == id_usuario,
        Tarea.fecha == fecha,
        Tarea.estado == estado
    )

    if id_turno is not None:
        query = query.filter(Tarea.id_turno == id_turno)

    return query.all()

