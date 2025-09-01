from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RendimientoRequest(BaseModel):
    lote_id: str
    cultivo: str

class RendimientoResponse(BaseModel):
    rendimiento_estimado: float
    confianza: float

@router.post("/", response_model=RendimientoResponse)
def predecir_rendimiento(request: RendimientoRequest):
    return RendimientoResponse(
        rendimiento_estimado=4500.0,
        confianza=0.75,
    )
