import asyncio
import aiohttp
from dataclasses import asdict
from src.utils.async_requests import async_request, HttpMethod
from src.animals.endpoints import get_destination_url
from src.animals.animal import AnimalDetails
from typing import List


async def send_animals(animals: List[AnimalDetails]):
    url = get_destination_url('home')
    json = [asdict(animal) for animal in animals]
    print(json)
    async with aiohttp.ClientSession() as session:
        data = await async_request(HttpMethod.POST, session, url, json=json)
    print(data)


def main():
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
    asyncio.run(send_animals(mocked_animals))
