from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NotificacionCreate(BaseModel):
    tipo: str
    contenido: str
    fecha_envio: datetime
    id_usuario_origen: Optional[int] = None
    id_usuario_destino: Optional[int] = None
    id_alarma: Optional[int] = None

class NotificacionOut(BaseModel):
    id_notificacion: int
    tipo: str
    contenido: str
    fecha_envio: datetime
    id_usuario_origen: Optional[int]
    id_usuario_destino: Optional[int]
    id_alarma: Optional[int]

    model_config = {
        "from_attributes": True
    }
