from pydantic import BaseModel
from datetime import date
from typing import Optional, Literal

class TareaCreate(BaseModel):
    descripcion: str
    estado: Literal["pendiente", "completada"]
    fecha: date
    duracion_minutos: int
    id_enfermero: Optional[int] = None
    id_turno: Optional[int] = None

class TareaOut(BaseModel):
    id_tarea: int
    descripcion: str
    estado: str
    fecha: date
    duracion_minutos: int
    id_enfermero: Optional[int]
    id_turno: Optional[int]

    model_config = {
        "from_attributes": True
    }
