from typing import Optional

from loguru import logger

from app.core import requests
from app.core import constants
from app.core import settings
from app import schemas


async def get_oauth2_credentials(code: str) -> Optional[schemas.VKAuthResponse]:
    """Getting the OAuth2 credentials for the user

    Args:
        code: The oauth2 code

    Returns:
        Optional[schemas.VKAuthResponse]
    """
    url = constants.VK_ACCESSS_TOKEN_URL.format(
        client_id=settings.VK_CLIENT_ID,
        client_secret=settings.VK_CLIENT_SECRET,
        redirect_uri=settings.VK_REDIRECT_URI,
        code=code,
    )
    try:
        response = await requests.get_json(url)
    except Exception as e:
        logger.info("Can't get OAuth2 credentials from %s", url)
        return None
    else:
        return schemas.VKAuthResponse(**response)
