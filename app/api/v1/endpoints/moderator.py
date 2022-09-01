from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app import schemas, crud

router = APIRouter()


@router.post("/", response_model=schemas.Moderator)
async def create_moderator(
    vk_id: int,
    steamid: int,
    *,
    session: Session = Depends(deps.get_session),
) -> Any:
    moderator = schemas.ModeratorCreate(vk_id=vk_id, steamid=steamid)
    moderator = await crud.moderator.create(session, obj_in=moderator)
    return moderator
