import asyncio
import aiohttp
from src.animals.send_animals import send_animals
from src.animals.animal import AnimalDetails

MOCKED_ANIMALS = [
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


async def send_mocked_animals():
    async with aiohttp.ClientSession() as session:
        n_saved = await send_animals(MOCKED_ANIMALS, session)
    print(f'Sent {n_saved} home.')


def run():
    asyncio.run(send_mocked_animals())
