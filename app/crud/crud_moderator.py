from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.crud.base import CRUDBase
from app.models.moderator import Moderator
from app.schemas.moderator import ModeratorCreate, ModeratorUpdate


class CRUDModerator(CRUDBase[Moderator, ModeratorCreate, ModeratorUpdate]):
    async def get_moderator_by_vk(
        self, db: AsyncSession, vk_id: int
    ) -> Optional[Moderator]:
        query = select(self.model).where(self.model.vk_id == vk_id)
        result = await db.execute(query)
        return result.first()


moderator = CRUDModerator(Moderator)
