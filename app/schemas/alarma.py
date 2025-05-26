from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

class AlarmaCreate(BaseModel):
    tipo: str
    descripcion: str
    estado: Literal["pendiente", "completada"]
    fecha: datetime
    id_usuario: Optional[int] = None
    id_residente: Optional[int] = None

class AlarmaOut(BaseModel):
    id_alarma: int
    tipo: str
    descripcion: str
    estado: str
    fecha: datetime
    id_usuario: Optional[int]
    id_residente: Optional[int]

    model_config = {
        "from_attributes": True
    }
