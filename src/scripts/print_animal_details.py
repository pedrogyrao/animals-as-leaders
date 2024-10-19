import asyncio
import aiohttp
import click

from src.animals.get_animal_details import get_animal_details


async def print_animal_details(animal_id):
    async with aiohttp.ClientSession() as session:
        animal_details = await get_animal_details(animal_id, session)
    print(animal_details)


@click.command()
@click.option('--animal_id')
def run(animal_id):
    asyncio.run(print_animal_details(animal_id))
