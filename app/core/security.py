from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import moderator


async def is_moderator(db: AsyncSession, vk_id: int) -> bool:
    moderator = await moderator.get_moderator_by_vk(db, vk_id)
    if moderator is None:
        return False
    return True
