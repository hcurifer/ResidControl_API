from fastapi import FastAPI
from app.api import example_router

app = FastAPI(title="ResidControl API")

# Incluir routers aquí
app.include_router(example_router.router)
