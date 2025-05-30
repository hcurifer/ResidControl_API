from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.usuario import Usuario
from passlib.context import CryptContext

# Crear el contexto de hash
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Datos del nuevo usuario
nuevo_usuario = {
    "nombre": "Usuario",
    "apellidos": "Prueba",
    "edad": 30,
    "email": "prueba@residcontrol.com",
    "contrasenia": "1234",  # contraseña sin hash
    "rol": "mando",
    "numero_empresa": "EMP9999"
}

# Función para insertar usuario
def crear_usuario():
    db: Session = SessionLocal()

    # Crear hash
    hash_contrasenia = pwd_context.hash(nuevo_usuario["contrasenia"])

    # Crear instancia del modelo
    usuario = Usuario(
        nombre=nuevo_usuario["nombre"],
        apellidos=nuevo_usuario["apellidos"],
        edad=nuevo_usuario["edad"],
        email=nuevo_usuario["email"],
        contrasenia_hash=hash_contrasenia,
        rol=nuevo_usuario["rol"],
        numero_empresa=nuevo_usuario["numero_empresa"]
    )

    try:
        db.add(usuario)
        db.commit()
        print("✅ Usuario creado con éxito")
    except Exception as e:
        print("❌ Error al crear usuario:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    crear_usuario()
