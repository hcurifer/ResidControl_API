# app/schemas/correo_schema.py

from pydantic import BaseModel, EmailStr

class PeticionDiaRequest(BaseModel):
    destinatario: EmailStr
    fecha: str
    nombre: str
    apellidos: str

class PeticionDiaInput(BaseModel):
    fecha: str
    nombre: str
    apellidos: str

class NotificacionAlarmaCorreo(BaseModel):
    tipo: str  
    descripcion: str
    mensaje: str
    enfermero: str
    residente: str
