from pydantic import BaseModel, EmailStr
from typing import Literal

# Para recibir datos al crear un usuario
class UsuarioCreate(BaseModel):
    nombre: str
    apellidos: str
    edad: Optional[int] = None
    email: EmailStr
    contrasenia: str
    rol: Literal["mando", "enfermero"]
    numero_empresa: str

# Para devolver datos en GET
class UsuarioOut(BaseModel):
    id_usuario: int
    nombre: str
    apellidos: str
    edad: Optional[int]
    email: EmailStr
    rol: Literal["mando", "enfermero"]
    numero_empresa: str

    model_config = {
        "from_attributes": True
    }
