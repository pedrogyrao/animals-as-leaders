import time
import asyncio
from typing import List
import aiohttp
from src.animals.animal import AnimalDetails
from src.animals.get_animal_details import get_animal_details
from src.animals.get_animal_list import get_total_pages, fetch_page
from src.animals.send_animals import send_animals
from src.utils.slice_list import slice_list

BATCH_SIZE = 100
EXECUTION_MESSAGE = '''Execution times:
\tGetting details: {get_details:.2f}s
\tSending home: {send_home:.2f}s
Total Time: {total_time:.2f}
'''


async def get_page_details(
    session: aiohttp.ClientSession,
    page_number: int
) -> List[AnimalDetails]:
    page = await fetch_page(session, page_number)
    get_details_tasks = [
        get_animal_details(animal.id, session) for animal in page.items
    ]
    return await asyncio.gather(*get_details_tasks)


def unpack_paged_details(paged_details):
    return [animal_detail for page in paged_details for animal_detail in page]


async def send_all_animals_home():
    execution_latencies = {}
    overall_ref = time.time()
    async with aiohttp.ClientSession() as session:
        total_pages = await get_total_pages(session)
        get_details_tasks = [
            get_page_details(session, page_number)
            for page_number in range(1, total_pages + 1)
        ]

        print('Getting animal details.')
        ref = time.time()
        paged_animal_details = await asyncio.gather(*get_details_tasks)
        execution_latencies['get_details'] = time.time() - ref

        animal_details = unpack_paged_details(paged_animal_details)
        print(f'Retrieved {len(animal_details)} details.')
        batches = slice_list(animal_details, BATCH_SIZE)
        send_animals_tasks = [send_animals(batch, session) for batch in batches]

        print('Sending animals home.')
        ref = time.time()
        send_results = await asyncio.gather(*send_animals_tasks)
        execution_latencies['send_home'] = time.time() - ref

    print(f'Sent {sum(send_results)} animals home!')

    execution_latencies['total_time'] = time.time() - overall_ref
    print(EXECUTION_MESSAGE.format(**execution_latencies))


def run():
    asyncio.run(send_all_animals_home())
