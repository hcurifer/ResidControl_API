# app/services/email_service.py

from email.message import EmailMessage
import aiosmtplib

# Configuración SMTP de Brevo
SMTP_HOST = "smtp-relay.brevo.com"
SMTP_PORT = 587
SMTP_USER = "TU_CORREO@mail.com"       # correo Brevo
SMTP_PASS = "TU_CONTRASEÑA_GENERADA"   # contraseña SMTP generada

# Función específica para PETICIÓN DE DÍA
async def enviar_peticion_dia(destinatario: str, fecha: str, nombre: str, apellidos: str):
    nombre_completo = f"{nombre} {apellidos}"
    asunto = "Petición de día"
    cuerpo = (
        f"Buenos Dias:,\n\n"
        f"{nombre_completo} ha solicitado el día {fecha}.\n"
        f"Por favor, revisa y responde si se aprueba o se rechaza.\n\n"
        f"—\n"
        f"Solicitado por: {nombre_completo}"
    )
    return await enviar_correo(destinatario, asunto, cuerpo)

# Función base reutilizable para cualquier correo
async def enviar_correo(destinatario: str, asunto: str, cuerpo: str):
    mensaje = EmailMessage()
    mensaje["From"] = SMTP_USER
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.set_content(cuerpo)

    try:
        await aiosmtplib.send(
            mensaje,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USER,
            password=SMTP_PASS
        )
        return True
    except Exception as e:
        print("❌ Error al enviar correo:", e)
        return False
