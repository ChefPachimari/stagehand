# Stagehand
This project will contain a django service that can be installed via pip for ease.

# Functionalities
Contains endpoints that can yield the diference between the **sum of squares** of the first N natural numbers against the **square of the sum** of the first N natural numbers.
For this project N is limited from 0 to 100

This project will assume frequent requests and be able to store additionalrudimentary data 

## Endpoints
GET /difference?number=N

return JSON
```
{
    "datetime": current timestamp,
    "value": return,
    "number": input N,
    "occurences": # of calls for this number,
    "last_datetime": timestamp of previous call
}
```


# Stack
please ensure your system is capable of running things.
Python 3.10+
Django 4.2+
Sqlite 3+
Redis 7+

# Installation

# TODO
* add functionality for a Pythagorean triplet where C is no greater than 1000 of the triplet.
* add unit testing
