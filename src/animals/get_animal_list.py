def get_animal_list():
    return [
        {'id': 4991, 'name': 'Turtle', 'born_at': None},
        {'id': 4995, 'name': 'Pony', 'born_at': 877863638315},
    ]


def print_animal_basic_information():
    for animal in get_animal_list():
        animal_id = animal['id']
        name = animal['name']
        born_at = animal['born_at']

        print(f'{animal_id}: {name}' + f' - born at {born_at}' if born_at else '')
