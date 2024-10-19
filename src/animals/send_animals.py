import re
import aiohttp
from dataclasses import asdict
from src.utils.async_requests import async_request, HttpMethod
from src.animals.endpoints import get_destination_url
from src.animals.animal import AnimalDetails
from typing import List


def parse_response(response):
    if not response or 'message' not in response:
        return 0
    match = re.search(r'Helped (\d+)', response['message'])
    return int(match.group(1)) if match else 0


async def send_animals(
    animals: List[AnimalDetails],
    session: aiohttp.ClientSession
) -> int:
    url = get_destination_url('home')
    json = [asdict(animal) for animal in animals]
    response = await async_request(HttpMethod.POST, session, url, json=json)
    return parse_response(response)
