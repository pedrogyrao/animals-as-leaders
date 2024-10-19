from setuptools import setup, find_packages

setup(
    name="animals-as-leaders",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "aiohttp",
        "click"
    ],
    extras_require={
        "dev": [
            "flake8",
            "pytest",
        ],
    },
    entry_points={
        'console_scripts': [
            'print_basic_info=src.scripts.print_animals_basic_information:run',
            'print_animal_details=src.scripts.print_animal_details:run',
            'send_animals=src.scripts.send_mocked_animals:run',
            'send_them_home=src.scripts.send_all_animals_home:run',
            'send_them_home_v2=src.scripts.send_all_animals_home_v2:run',
        ],
    },
)
