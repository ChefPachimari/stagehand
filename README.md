# Stagehand
This practice problem will contain a django service containing functionalities for various computations and utilities

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
# Initial Installation
1. Clone the project via Git.
2. Read through or run `initial_dev.sh`
    a. this will build the venv, install requirements.txt packages, migrate, generate and load fixtures.
3. run `source venv/bin/activate`
4. run `python manage.py`

# Stack
please ensure your system is capable of running things.
* Python 3.10+
* Django 4.2+
* Sqlite 3+

# TODO
* [DONE] add functionality for a Pythagorean triplet where C is no greater than 1000 of the triplet.
* [DONE] add unit testing
