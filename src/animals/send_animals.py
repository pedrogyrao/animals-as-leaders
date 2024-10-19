import asyncio
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


async def send_mocked_animals():
    mocked_animals = [
        AnimalDetails(
            id=1,
            name='Ant',
            born_at=None,
            friends=['Goldfish', 'Gerbil', 'Penguin', 'Partridge']
        ),
        AnimalDetails(
            id=2,
            name='Albatross',
            born_at=None,
            friends=['Goose', 'Goshawk', 'Hamster']
        ),
        AnimalDetails(
            id=3,
            name='Crane',
            born_at=None,
            friends=''
        ),
        AnimalDetails(
            id=5,
            name='Sand Dollar',
            born_at='2010-05-23T18:22:30.880Z',
            friends=['Rat', 'Seahorse', 'Jay', 'Curlew']
        ),
    ]
    async with aiohttp.ClientSession() as session:
        n_saved = await send_animals(mocked_animals, session)
    print(f'Sent {n_saved} home.')


def main():
    asyncio.run(send_mocked_animals())
