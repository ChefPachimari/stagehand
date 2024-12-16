#!/bin/bash

# Create a virtual environment named 'venv'

# Prompt the user to confirm Redis installation
# read -p "Redis will be installed on the system. Do you want to continue? (y/n): " confirm
# if [[ $confirm != [yY] ]]; then
#     echo "Redis installation aborted."
#     exit 1
# fi

# # Install Redis
# sudo apt-get update
# sudo apt-get install -y redis-server

python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Initial Install the dependencies from requirements.txt
pip install -r requirements.txt

echo "venv set up and ready to use, run 'source venv/bin/activate'"