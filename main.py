from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import usuario_router
from app.api import residente_router

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
