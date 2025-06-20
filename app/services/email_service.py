# app/services/email_service.py

from email.message import EmailMessage
import aiosmtplib
import os
from dotenv import load_dotenv

load_dotenv() #Carga las variables del archivo .env

# Configuración SMTP de Brevo
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))  
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")


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


# Función específica para NOTIFICACIÓN
async def enviar_correo_notificacion_alarma(
    tipo: str,
    descripcion: str,
    mensaje: str,
    enfermero: str,
    residente: str
):
    asunto = "Notificación sobre la alarma"
    cuerpo = f"""
IMPORTANTE: notificación sobre alarma

Tipo: {tipo.upper()}
Alarma: {descripcion}
Residente: {residente}
Asignada a: {enfermero}

Mensaje de notificación:
{mensaje}

Se solicita que esta alarma sea tratada con la mayor brevedad posible.
""".strip()

    return await enviar_correo(
        destinatario="ResidControl@protonmail.com",
        asunto=asunto,
        cuerpo=cuerpo
    )

# Función base reutilizable para cualquier correo
async def enviar_correo(destinatario: str, asunto: str, cuerpo: str, remitente: str = None):

    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT"))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")

    mensaje = EmailMessage()
    mensaje["From"] =  SMTP_USER
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



