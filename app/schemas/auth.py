from pydantic import BaseModel


class VKAuthRequest(BaseModel):
    code: str


class VKAuthResponse(BaseModel):
    access_token: str
    expires_in: int
    user_id: int
