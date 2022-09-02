from typing import Optional, Any

import aiohttp
from aiohttp.typedefs import StrOrURL


async def _request(
    url: StrOrURL,
    method: str = "GET",
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    headers: Optional[dict[str, str]] = None,
    session: aiohttp.ClientSession = None,
    **kwargs: Any,
) -> aiohttp.ClientResponse:
    """Raw request for any HTTP method and parameters.

    Args:
        url: string or URL to request
        method: HTTP method. Default "GET"
        params: query parameters. Default None
        data: body parameters. Default None
        headers: custom headers. Default None
        session: aiohttp client session instance. Default None

    Returns:
        aiohttp.ClientResponse instance
    """
    if session is None:
        session = aiohttp.ClientSession()
    if headers is not None:
        session.headers.update(headers)

    async with session.request(
        method=method, url=url, params=params, data=data, **kwargs
    ) as response:
        await response.read()
        return response


async def _request_json(
    url: StrOrURL,
    method: str = "GET",
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    session: aiohttp.ClientSession = None,
    **kwargs: Any,
) -> dict:
    """Raw requests which return json."""
    response = await _request(url, method, params, data=data, session=session, **kwargs)
    return await response.json(encoding="utf-8", content_type=None)


async def get_json(
    url: StrOrURL,
    params: Optional[dict] = None,
    session: aiohttp.ClientSession = None,
    **kwargs: Any,
) -> dict:
    """HTTP GET request which return json."""
    return await _request_json(url, "GET", params, session=session, **kwargs)
