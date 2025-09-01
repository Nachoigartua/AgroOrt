from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter()

class SiembraRequest(BaseModel):
    lote_id: str
    cliente_id: str
    cultivo: str
    latitud: Optional[float] = Field(None, description="Latitud del lote")
    longitud: Optional[float] = Field(None, description="Longitud del lote")

class SiembraResponse(BaseModel):
    fecha_recomendada: str
    alternativas: list[str]
    confianza: float

@router.post("/", response_model=SiembraResponse)
def recomendar_siembra(request: SiembraRequest):
    # Placeholder logic
    return SiembraResponse(
        fecha_recomendada="2024-06-01",
        alternativas=["2024-05-25", "2024-06-05"],
        confianza=0.8,
    )
