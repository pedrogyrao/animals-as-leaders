import asyncio
import aiohttp
import click
from typing import Union
from src.animals.animal import AnimalDetails
from src.utils.async_requests import async_request, HttpMethod
from src.animals.endpoints import get_origin_url


async def get_animal_details(animal_id: str) -> Union[AnimalDetails, None]:
    url = get_origin_url('animal_details', animal_id=animal_id)
    async with aiohttp.ClientSession() as session:
        data = await async_request(HttpMethod.GET, session, url)
        return AnimalDetails(**data) if data else None


async def print_animal_details(animal_id):
    animal_details = await get_animal_details(animal_id)
    print(animal_details)


@click.command()
@click.option('--animal_id')
def main(animal_id):
    asyncio.run(print_animal_details(animal_id))
