from fastapi import APIRouter, HTTPException
from app.services.email_service import enviar_peticion_dia
from app.schemas.correo_schema import PeticionDiaRequest

router = APIRouter(prefix="/correo", tags=["Correo"])

@router.post("/peticion-dia")
async def peticion_dia(data: PeticionDiaRequest):
    enviado = await enviar_peticion_dia(
        destinatario=data.destinatario,
        fecha=data.fecha,
        nombre=data.nombre,
        apellidos=data.apellidos
    )

    if not enviado:
        raise HTTPException(status_code=500, detail="Error al enviar el correo")

    return {"mensaje": "Correo de petición de día enviado correctamente"}
