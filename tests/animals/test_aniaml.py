from src.animals.animal import AnimalDetails, AnimalPage, AnimalBasicInfo

SEC_TO_MILLS = 1000


def test_animal_details_initialization():
    animal = AnimalDetails(id=1, name="Dog", born_at=676351245682, friends="Cat, Bird")

    assert animal.id == 1
    assert animal.name == "Dog"

    expected_born_at = '1991-06-08T03:20:45.682Z'
    assert animal.born_at == expected_born_at

    assert animal.friends == ["Cat", "Bird"]


def test_animal_page_initialization():
    raw_data = {
        "page": 1,
        "total_pages": 3,
        "items": [
            {"id": 1, "name": "Dog", "born_at": 676351245682},
            {"id": 2, "name": "Cat", "born_at": None}
        ]
    }
    animal_page = AnimalPage(**raw_data)

    assert animal_page.page == 1
    assert animal_page.total_pages == 3
    assert len(animal_page.items) == 2

    animal1, animal2 = animal_page.items
    assert isinstance(animal1, AnimalBasicInfo)
    assert animal1.id == 1
    assert animal1.name == "Dog"
    assert animal1.born_at == 676351245682

    assert isinstance(animal2, AnimalBasicInfo)
    assert animal2.id == 2
    assert animal2.name == "Cat"
    assert animal2.born_at is None
