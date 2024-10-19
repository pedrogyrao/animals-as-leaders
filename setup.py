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
            'print_basic_info=src.animals.get_animal_list:main',
            'print_animal_details=src.animals.get_animal_details:main',
            'send_animals=src.animals.send_animals:main',
        ],
    },
)
