from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AgroquimicoRequest(BaseModel):
    lote_id: str
    cultivo: str

class AgroquimicoResponse(BaseModel):
    cronograma: list[str]

@router.post("/", response_model=AgroquimicoResponse)
def recomendar_agroquimicos(request: AgroquimicoRequest):
    return AgroquimicoResponse(
        cronograma=["Aplicar insecticida X al día 20", "Aplicar fungicida Y al día 40"],
    )
