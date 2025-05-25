from app.db.session import SessionLocal
from sqlalchemy import text

def probar_conexion():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  
        print("Conexión a PostgreSQL exitosa.")
    except Exception as e:
        print("Error al conectar con PostgreSQL:", e)
    finally:
        db.close()

probar_conexion()
