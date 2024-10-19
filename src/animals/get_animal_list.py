import time
import asyncio
import aiohttp
from src.utils.async_requests import async_request, HttpMethod
from src.animals.endpoints import get_origin_url
from src.animals.animal import AnimalBasicInfo, AnimalPage
from typing import List


def parse_pages(pages: List[AnimalPage]) -> List[AnimalBasicInfo]:
    return [AnimalBasicInfo(animal) for page in pages for animal in page.items]


async def fetch_page(session, url, page_number) -> AnimalPage:
    params = {"page": page_number}
    response = await async_request(HttpMethod.GET, session, url, params)
    return AnimalPage(**(response if response else {}))


async def get_animal_list() -> List[AnimalBasicInfo]:
    url = get_origin_url('list_animals')

    async with aiohttp.ClientSession() as session:
        page_0 = await fetch_page(session, url, 0)
        total_pages = page_0.total_pages

        print(f'Retrieving {total_pages} pages')

        tasks = [fetch_page(session, url, page) for page in range(1, total_pages + 1)]
        pages = await asyncio.gather(*tasks)

    return parse_pages(pages)


async def print_animal_basic_information():
    time_ref = time.time()
    animals = await get_animal_list()
    time_end = time.time()

    for a in animals:
        print(f'{a.id}: {a.name}' + (f' - born at {a.born_at}' if a.born_at else ''))

    print(f'It took {time_end - time_ref} s to retrieve all {len(animals)} animals')


def main():
    asyncio.run(print_animal_basic_information())
