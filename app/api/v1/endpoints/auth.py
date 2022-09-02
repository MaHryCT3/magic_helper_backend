import secrets
from typing import Union

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import schemas
from app import crud
from app.api import deps
from app.core import security
from app.services import vk

router = APIRouter()


@router.get(
    "/vk",
    response_model=schemas.VKSuccessAuthResponse,
    responses={status.HTTP_400_BAD_REQUEST: {"model": schemas.ErrorResponse}},
)
async def vk_auth(
    code: str,
    *,
    session: Session = Depends(deps.get_session),
) -> Union[JSONResponse, schemas.VKAuthResponse]:
    oauth2_credentials = await vk.get_oauth2_credentials(code)

    if oauth2_credentials is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=schemas.ErrorResponse(
                message="unable to get oauth2 credentials from vk",
            ).dict(),
        )

    vk_id = oauth2_credentials.user_id

    moderator = await crud.moderator.get_moderator_by_vk(session, vk_id)

    if moderator is None:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=schemas.ErrorResponse(
                message="ты не модератор",
            ).dict(),
        )

    access_token = oauth2_credentials.access_token
    token_object = await crud.token.get_token_by_vk(session, vk_id)
    bearer_token = secrets.token_hex(32)

    if token_object is None:
        await crud.token.create_token(session, vk_id, bearer_token, access_token)
    else:
        await crud.token.update_token(session, token_object, bearer_token, access_token)

    return schemas.VKSuccessAuthResponse(token=bearer_token)
