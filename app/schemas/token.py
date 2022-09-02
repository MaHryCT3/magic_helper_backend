from typing import Optional
from datetime import datetime, timedelta

from pydantic import BaseModel


class TokenBase(BaseModel):
    vk_id: int
    bearer_token: str
    access_token: str
    expires: datetime


class TokenCreate(TokenBase):
    expires: datetime = datetime.now() + timedelta(days=7)


class TokenUpdate(TokenBase):
    pass


class TokenInDBBase(TokenBase):
    class Config:
        orm_mode = True


class Token(TokenInDBBase):
    pass
