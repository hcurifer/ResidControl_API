from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeedbackCreate(BaseModel):
    tipo: str
    contenido: str
    fecha: datetime
    id_usuario: Optional[int] = None

class FeedbackOut(BaseModel):
    id_feedback: int
    tipo: str
    contenido: str
    fecha: datetime
    id_usuario: Optional[int]

    model_config = {
        "from_attributes": True
    }
