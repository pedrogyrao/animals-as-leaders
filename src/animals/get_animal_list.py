import asyncio
import aiohttp
from src.utils.async_requests import async_request, HttpMethod
from src.animals.endpoints import get_origin_url
from src.animals.animal import AnimalBasicInfo, AnimalPage
from typing import List


def parse_pages(pages: List[AnimalPage]) -> List[AnimalBasicInfo]:
    return [AnimalBasicInfo(**animal) for page in pages for animal in page.items]


async def fetch_page(session, url, page_number) -> AnimalPage:
    params = {"page": page_number}
    response = await async_request(HttpMethod.GET, session, url, params)
    return AnimalPage(**(response if response else {}))


async def get_animal_list(session: aiohttp.ClientSession) -> List[AnimalBasicInfo]:
    url = get_origin_url('list_animals')
    page_0 = await fetch_page(session, url, 0)
    total_pages = page_0.total_pages

    print(f'Retrieving {total_pages} pages')
    tasks = [fetch_page(session, url, page) for page in range(1, total_pages + 1)]
    pages = await asyncio.gather(*tasks)
    return parse_pages(pages)
