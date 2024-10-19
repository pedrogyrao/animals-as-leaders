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
