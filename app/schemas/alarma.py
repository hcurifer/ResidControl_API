from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

class AlarmaCreate(BaseModel):
    descripcion: str
    estado: Literal["pendiente", "completada"]
    fecha: datetime
    id_usuario: Optional[int] = None
    id_residente: Optional[int] = None

class AlarmaOut(BaseModel):
    id_alarma: int
    descripcion: str
    estado: str
    fecha: datetime
    id_usuario: Optional[int]
    id_residente: Optional[int]

    model_config = {
        "from_attributes": True
    }
class AlarmaConNombres(BaseModel):
    id_alarma: int
    descripcion: str
    estado: str
    fecha: datetime
    enfermero: Optional[str]
    residente: Optional[str]

    model_config = {
        "from_attributes": True
    }
