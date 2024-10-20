# Animals as Leaders


![plot](./assets/animals-as-leaders.webp)
https://youtu.be/gu-_kyU4dWk

----

`Animals as Leaders` is a Python project made to unravel the animal world and helping getting them home!

The basic idea here is:

1. retrieve all the animal ids by getting all the pages from `/animals/v1/animals?page=<number>`
2. get all the animal details from `/animals/v1/animals/<animal-id>`
3. transform the data to respect home format
3. send (*post*) them home in big batches (of 100 animals) using `/animals/v1/home`

Problems:

* System throws:
    * Internal Server Error (500)
    * Bad Gateway (502)
    * Service Unavailable (503)
    * Gateway Timeout (504)

So we will have to retry on those

* System shows random latency time to time (sleeps of 5 to 15 seconds). So our system will have to either timeout and try again, or make sure it waits.

## Scripts

To run the scripts, first install the package by running

```bash
pip install -e .
```

then use:

* `print_basic_info` - lists all animals basic information by getting all pages from `/animals/v1/animals?page=<number>` and printing animal information.
* `print_animal_details --animal_id <id>` - gets the detail of the animal id provided from `/animals/v1/animals/<animal-id>`
* `send_animals` - sends some mocked animals home by posting them on `/animals/v1/home`
* `send_them_home` - V1 version of the main script
* `send_them_home_v2` - V2 version of the main script

## Send them home V1

For the first version I leveraged `asyncio` to not be blocked by response times. But it is still a very simple/straight forward solution.

1. lists all animals by going through all pages
1. get all animal details
1. organize data in batches of 100 animal details
1. send batches home

Executions times:
```
Listing animals: 9.65s
Getting details: 18.66s
Sending home: 0.21s
Total Time: 28.52
```

## Send them home V2

Checking execution times from V1, we can identify some latency issues:

* the biggest latency is caused by getting details
* we are wasting time waiting for all the listings to finish before starting getting details

This version combines getting a page and immediately retrieving the page's animal details.

Execution times:
```
Getting details: 17.76s
Sending home: 0.20s
Total Time: 17.98
```

## Tests

To run tests run:

```bash
pip install -e [dev]
pytest
```

I only added tests around `async_request` function. But ideally I would like to add tests to everything.
