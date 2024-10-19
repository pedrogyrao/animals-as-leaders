import asyncio
import aiohttp
from src.utils.async_requests import async_request, HttpMethod
from src.animals.endpoints import get_origin_url
from src.animals.animal import AnimalBasicInfo, AnimalPage
from typing import List

EMPTY_PAGE_ZERO = 0


def get_basic_info_from_pages(pages: List[AnimalPage]) -> List[AnimalBasicInfo]:
    return [basic_info for page in pages for basic_info in page.items]


async def fetch_page(session: aiohttp.ClientSession, page_number: int) -> AnimalPage:
    params = {"page": page_number}
    url = get_origin_url('list_animals')
    response = await async_request(HttpMethod.GET, session, url, params)
    return AnimalPage(**(response if response else {}))


async def get_total_pages(session: aiohttp.ClientSession) -> int:
    page_0 = await fetch_page(session, EMPTY_PAGE_ZERO)
    return page_0.total_pages


async def get_animal_list(session: aiohttp.ClientSession) -> List[AnimalBasicInfo]:
    total_pages = await get_total_pages(session)

    print(f'Retrieving {total_pages} pages')
    tasks = [fetch_page(session, page) for page in range(1, total_pages + 1)]
    pages = await asyncio.gather(*tasks)
    return get_basic_info_from_pages(pages)
