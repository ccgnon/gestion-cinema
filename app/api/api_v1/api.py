from fastapi import APIRouter

from app.api.api_v1.endpoints import film,auth


api_router = APIRouter()
api_router.include_router(film.router, prefix="/films", tags=["films"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])