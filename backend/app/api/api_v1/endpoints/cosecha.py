from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CosechaRequest(BaseModel):
    lote_id: str
    cultivo: str

class CosechaResponse(BaseModel):
    fecha_optima: str
    ventana: list[str]

@router.post("/", response_model=CosechaResponse)
def recomendar_cosecha(request: CosechaRequest):
    return CosechaResponse(
        fecha_optima="2024-12-01",
        ventana=["2024-11-20", "2024-12-10"],
    )
