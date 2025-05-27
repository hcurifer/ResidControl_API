from pydantic import BaseModel
from datetime import date
from typing import Optional, Literal

class ResidenteCreate(BaseModel):
    nombre: str
    apellidos: str
    edad: Optional[int] = None
    estado: Literal["en residencia", "fuera", "ingresado"]
    habitacion: str
    ubicacion: Optional[str] = None
    fecha_ingreso: Optional[date] = None

class ResidenteOut(BaseModel):
    id_residente: int
    nombre: str
    apellidos: str
    edad: Optional[int]
    estado: str
    habitacion: str
    ubicacion: Optional[str] = None
    fecha_ingreso: Optional[date] = None

    model_config = {
        "from_attributes": True
    }
