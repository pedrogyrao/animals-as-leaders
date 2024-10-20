
from typing import Any, Dict, Tuple
from enum import Enum
from aiohttp import ClientSession

RETRY_STATUS_CODE = {500, 502, 503, 504}
MAX_RETRIES = 3
STATUS_IGNORED_MESSAGE = 'Ignoring status {} for params {} url {}'
ERROR_IGNORED_MESSAGE = 'Ignoring exception {} for params {} url {}'
MAX_ATTEMPTS_MESSAGE = 'Attempted {} requests, ignoring params {} url {}'
INVALID_METHOD_MESSAGE = 'Invalid method {}, ignoring params {} url {}'


class HttpMethod(Enum):
    POST = 'POST'
    GET = 'GET'


async def async_request(
    method: HttpMethod,
    session: ClientSession,
    url: str,
    params: Dict[str, Any] = {},
    json: Dict[str, Any] = {},
    retry_on_status: Tuple[int] = RETRY_STATUS_CODE,
    max_retries: int = MAX_RETRIES
) -> Any:
    try:
        for _ in range(max_retries):
            if method == HttpMethod.GET:
                response = await session.get(url, params=params)
            elif method == HttpMethod.POST:
                response = await session.post(url, params=params, json=json)
            else:
                print(INVALID_METHOD_MESSAGE.format(method, params, url))
                return

            if response.status in retry_on_status:
                continue

            if response.ok:
                return await response.json()

            print(STATUS_IGNORED_MESSAGE.format(response.status, params, url))
            return
        else:
            print(MAX_ATTEMPTS_MESSAGE.format(max_retries, params, url))
            return

    except Exception as error:
        print(ERROR_IGNORED_MESSAGE.format(error, params, url))
        return
