from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ClimaRequest(BaseModel):
    region: str

class ClimaResponse(BaseModel):
    precipitacion_mm: float
    temperatura_max: float
    temperatura_min: float

@router.post("/", response_model=ClimaResponse)
def predecir_clima(request: ClimaRequest):
    return ClimaResponse(
        precipitacion_mm=100.0,
        temperatura_max=30.0,
        temperatura_min=15.0,
    )
