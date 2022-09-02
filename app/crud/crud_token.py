from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.crud.base import CRUDBase
from app.models.token import Token
from app.schemas.token import TokenCreate, TokenUpdate


class CRUDToken(CRUDBase[Token, TokenCreate, TokenUpdate]):
    async def get_token_by_vk(self, db: AsyncSession, vk_id: int) -> Optional[Token]:
        query = select(self.model).where(self.model.vk_id == vk_id)
        result = await db.execute(query)
        return result.first()

    async def create_token(
        self,
        db: AsyncSession,
        vk_id: int,
        bearer_token: str,
        access_token: str,
    ) -> Token:
        obj_in = TokenCreate(
            vk_id=vk_id,
            bearer_token=bearer_token,
            access_token=access_token,
        )

        await self.create(db, obj_in=obj_in)
        return obj_in

    async def update_token(
        self, db: AsyncSession, token_obj: Token, bearer_token: str, access_token: str
    ) -> Token:
        token_in = TokenUpdate(
            vk_id=token_obj.vk_id,
            bearer_token=bearer_token,
            access_token=access_token,
        )
        await self.update(db, db_obj=token_obj, obj_in=token_in)
        return token_in


token = CRUDToken(Token)
