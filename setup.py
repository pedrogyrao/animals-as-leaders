from setuptools import setup, find_packages

setup(
    name="animals-as-leaders",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    extras_require={
        "dev": [
            "flake8",
            "pytest",
        ],
    },
    entry_points={
        'console_scripts': [
            'print_basic_info=src.animals.get_animal_list:print_animal_basic_information',
        ],
    },
)
