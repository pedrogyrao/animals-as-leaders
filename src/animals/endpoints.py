ORIGIN_BASE_URL = 'http://localhost:3123'
ORIGIN_ENDPOINTS = {
    'list_animals': '/animals/v1/animals',
    'animal_details': '/animals/v1/animals/{animal_id}',
}

DESTINATION_BASE_URL = 'http://localhost:3123'
DESTINATION_ENDPOINTS = {
    'home': '/animals/v1/home',
}


def get_origin_url(endpoint_name: str, **params) -> str:
    return ORIGIN_BASE_URL + ORIGIN_ENDPOINTS[endpoint_name].format(**params)


def get_destination_url(endpoint_name: str, **params) -> str:
    return DESTINATION_BASE_URL + DESTINATION_ENDPOINTS[endpoint_name].format(**params)
