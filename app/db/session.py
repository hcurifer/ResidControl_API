from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Crear motor de conexión
engine = create_engine(settings.DB_URL, echo=True)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
