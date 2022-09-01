from fastapi import APIRouter

from app.api.v1.endpoints import moderator

api_router = APIRouter()
api_router.include_router(moderator.router, prefix="/moderators")
