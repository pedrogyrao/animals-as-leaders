
from typing import Any, Dict, Tuple
from aiohttp import ClientSession

RETRY_STATUS_CODE = {500, 502, 503, 504}
MAX_RETRIES = 3
STATUS_IGNORED_MESSAGE = 'Ignoring status {status} for params {params} url {url}'
ERROR_IGNORED_MESSAGE = 'Ignoring exception {error} for params {params} url {url}}'
MAX_ATTEMPTS_MESSAGE = 'Attempted {number} requests, ignoring params {params} url {url}'


async def async_get(
    session: ClientSession,
    url: str,
    params: Dict[str, Any],
    retry_on_status: Tuple[int] = RETRY_STATUS_CODE,
    max_retries: int = MAX_RETRIES
) -> Any:
    try:
        for _ in range(max_retries):
            async with session.get(url, params=params) as response:
                if response.status in retry_on_status:
                    continue

                if response.ok:
                    return await response.json()

                print(STATUS_IGNORED_MESSAGE.format(response.status, params, url))
                return None
        else:
            print(MAX_ATTEMPTS_MESSAGE.format(max_retries, params, url))
            return None

    except Exception as e:
        print(ERROR_IGNORED_MESSAGE.format(e, params, url))
        return None
