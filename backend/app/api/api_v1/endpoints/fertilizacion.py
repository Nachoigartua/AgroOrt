from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FertilizacionRequest(BaseModel):
    lote_id: str
    cultivo: str

class FertilizacionResponse(BaseModel):
    plan: list[str]
    costo_estimado: float

@router.post("/", response_model=FertilizacionResponse)
def recomendar_fertilizacion(request: FertilizacionRequest):
    return FertilizacionResponse(
        plan=["Aplicar 100kg/ha de urea al inicio", "Aplicar 50kg/ha de fosfato a los 30 días"],
        costo_estimado=150.0,
    )
