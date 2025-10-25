from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VariedadRequest(BaseModel):
    lote_id: str
    cultivo: str

class VariedadResponse(BaseModel):
    variedad_principal: str
    alternativas: list[str]
    justificacion: str

@router.post("/", response_model=VariedadResponse)
def recomendar_variedad(request: VariedadRequest):
    return VariedadResponse(
        variedad_principal="Trigo INTA 123",
        alternativas=["Trigo INTA 456", "Trigo INTA 789"],
        justificacion="Variedad adaptada a la zona",
    )
