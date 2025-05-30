from fastapi import APIRouter, HTTPException, Depends
from app.services.email_service import enviar_peticion_dia
from app.schemas.correo_schema import PeticionDiaRequest
from app.schemas.correo_schema import PeticionDiaInput
from app.services.email_service import enviar_correo

router = APIRouter(
    prefix="/correo",
     tags=["Correo"]
     )

@router.post("/peticion-dia")
async def peticion_dia(data: PeticionDiaInput):
    asunto = "Petición de día"
    cuerpo = (
        f"Hola,\n\n"
        f"{data.nombre} {data.apellidos} ha solicitado el día {data.fecha}.\n"
        f"Por favor, revisa y responde si se aprueba o se rechaza.\n\n"
        f"—\n"
        f"Solicitado por: {data.nombre} {data.apellidos}"
    )

    enviado = await enviar_correo(
        destinatario="ResidControl@protonmail.com",
        asunto=asunto,
        cuerpo=cuerpo,
        
    )

    if not enviado:
        raise HTTPException(status_code=500, detail="No se pudo enviar el correo")

    return {"mensaje": "Correo enviado correctamente"}