from src.animals.animal import AnimalBasicInfo


def get_animal_list() -> list[AnimalBasicInfo]:
    return [
        AnimalBasicInfo(4991, 'Turtle', None),
        AnimalBasicInfo(4995, 'Pony', 877863638315),
    ]


def print_animal_basic_information():
    for a in get_animal_list():
        print(f'{a.id}: {a.name}' + (f' - born at {a.born_at}' if a.born_at else ''))
