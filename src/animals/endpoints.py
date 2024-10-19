ORIGIN_BASE_URL = 'http://localhost:3123'
ORIGIN_ENDPOINTS = {
    'list_animals': '/animals/v1/animals',
    'animal_details': '/animals/v1/animals/{animal_id}',
}


def get_origin_url(endpoint_name: str, **params) -> str:
    return f'{ORIGIN_BASE_URL}{ORIGIN_ENDPOINTS[endpoint_name]}'.format(params)
