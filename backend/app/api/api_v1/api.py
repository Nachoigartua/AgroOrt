from fastapi import APIRouter
from .endpoints import siembra, variedades, clima, fertilizacion, agroquimicos, rendimiento, cosecha

api_router = APIRouter()
api_router.include_router(siembra.router, prefix="/recomendaciones/siembra", tags=["siembra"])
api_router.include_router(variedades.router, prefix="/recomendaciones/variedades", tags=["variedades"])
api_router.include_router(clima.router, prefix="/recomendaciones/clima", tags=["clima"])
api_router.include_router(fertilizacion.router, prefix="/recomendaciones/fertilizacion", tags=["fertilizacion"])
api_router.include_router(agroquimicos.router, prefix="/recomendaciones/agroquimicos", tags=["agroquimicos"])
api_router.include_router(rendimiento.router, prefix="/recomendaciones/rendimiento", tags=["rendimiento"])
api_router.include_router(cosecha.router, prefix="/recomendaciones/cosecha", tags=["cosecha"])
