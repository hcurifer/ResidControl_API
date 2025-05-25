from fastapi import APIRouter

router = APIRouter(prefix="/example", tags=["Ejemplo"])

@router.get("/")
def ejemplo_basico():
    return {"mensaje": "Hola desde el router de ejemplo"}
