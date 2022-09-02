from app.schemas.responses.base import BaseResponse


class VKSuccessAuthResponse(BaseResponse):
    status: str = "success"
    token: str
