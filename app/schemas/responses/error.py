from app.schemas.responses.base import BaseResponse


class ErrorResponse(BaseResponse):
    status = "failure"
    message: str
