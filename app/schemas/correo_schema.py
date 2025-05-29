# app/schemas/correo_schema.py

from pydantic import BaseModel, EmailStr

class PeticionDiaRequest(BaseModel):
    destinatario: EmailStr
    fecha: str
    nombre: str
    apellidos: str
