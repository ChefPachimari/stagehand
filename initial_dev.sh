#!/bin/bash

# Create a virtual environment named 'venv'

# Prompt the user to confirm Redis installation
# read -p "Redis will be installed on the system. Do you want to continue? (y/n): " confirm
# if [[ $confirm != [yY] ]]; then
#     echo "Redis installation aborted."
#     exit 1
# fi

# # Install Redis
# holding off on redis as out of scope to think about putting a redis cache in front of the database just yet to handle load
# sudo apt-get update
# sudo apt-get install -y redis-server

python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Initial Install the dependencies from requirements.txt
pip install -r requirements.txt
python3 ./manage.py migrate
python3 ./manage.py generate_fixtures
python ./manage.py loaddata toolbox/fixtures/numbers_fixture.json

echo "venv set up and ready to use, run 'source venv/bin/activate'"