# AgroOrt ML Recommendation System

Este proyecto proporciona un esqueleto inicial para un sistema de recomendaciones agrícolas basado en Machine Learning según la Especificación Funcional (EF) y la Especificación Técnica (ET).

## Estructura

- `backend/app/main.py`: Aplicación FastAPI principal.
- `backend/app/api/api_v1/`: Endpoints agrupados por módulo de recomendación.
- `tests/`: Pruebas unitarias básicas de los endpoints.

## Ejecutar la aplicación

```bash
uvicorn backend.app.main:app --reload
```

## Ejecutar pruebas

```bash
pytest
```

Se requieren las dependencias definidas en `pyproject.toml`.
