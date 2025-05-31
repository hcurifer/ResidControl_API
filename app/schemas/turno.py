from pydantic import BaseModel
from datetime import date
from typing import Optional, Literal

class TurnoCreate(BaseModel):
    tipo_turno: Literal["mañana", "tarde", "noche"]
    fecha: date
    id_usuario: Optional[int] = None

class TurnoOut(BaseModel):
    id_turno: int
    tipo_turno: str
    fecha: date
    id_usuario: Optional[int]

    model_config = {
        "from_attributes": True
    }
