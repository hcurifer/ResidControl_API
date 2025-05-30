from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import usuario_router
from app.api import residente_router
from app.api import tarea_router
from app.api import turno_router
from app.api import alarma_router
from app.api import notificacion_router
from app.api import feedback_router
from app.api import correo_router

app = FastAPI(title="ResidControl API")

# CORS para permitir peticiones desde Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(usuario_router.router)
app.include_router(residente_router.router)
app.include_router(tarea_router.router)
app.include_router(turno_router.router)
app.include_router(alarma_router.router)
app.include_router(notificacion_router.router)
app.include_router(feedback_router.router)
app.include_router(correo_router.router)

for route in app.routes:
    print(f"🔗 {route.path}")
