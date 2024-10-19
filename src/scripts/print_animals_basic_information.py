import asyncio
import time
import aiohttp

from src.animals.get_animal_list import get_animal_list


async def print_animal_basic_information():
    async with aiohttp.ClientSession() as session:
        time_ref = time.time()
        animals = await get_animal_list(session)
        time_end = time.time()

    for a in animals:
        print(f'{a.id}: {a.name}' + (f' - born at {a.born_at}' if a.born_at else ''))

    print(f'It took {time_end - time_ref} s to retrieve all {len(animals)} animals')


def run():
    asyncio.run(print_animal_basic_information())
