from typing import Optional

from pydantic import BaseModel


class ModeratorBase(BaseModel):
    vk_id: Optional[int] = None
    steamid: Optional[int] = None


class ModeratorCreate(ModeratorBase):
    vk_id: int


class ModeratorUpdate(ModeratorBase):
    pass


class ModeratorInDBBase(ModeratorBase):
    vk_id: int
    steamid: int
    is_superuser: bool

    class Config:
        orm_mode = True


# Properties to return to client
class Moderator(ModeratorInDBBase):
    pass


class ModeratorInDB(ModeratorInDBBase):
    pass
