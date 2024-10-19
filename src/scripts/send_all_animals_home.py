import time
import asyncio
import aiohttp
import json as JSON
from src.animals.get_animal_details import get_animal_details
from src.animals.get_animal_list import get_animal_list
from src.animals.send_animals import send_animals
from src.utils.slice_list import slice_list

BATCH_SIZE = 100
EXECUTION_MESSAGE = '''Execution times:
\tListing animals: {list_animals:.2f}s
\tGetting details: {get_details:.2f}s
\tSending home: {send_home:.2f}s
Total Time: {total_time:.2f}
'''


async def send_all_animals_home():
    execution_latencies = {}
    overall_ref = time.time()
    async with aiohttp.ClientSession() as session:
        print('Listing animals.')
        ref = time.time()
        animals = await get_animal_list(session)
        execution_latencies['list_animals'] = time.time() - ref

        get_details_tasks = [
            get_animal_details(animal.id, session) for animal in animals
        ]

        print('Getting animal details.')
        ref = time.time()
        animal_details = await asyncio.gather(*get_details_tasks)
        execution_latencies['get_details'] = time.time() - ref

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
