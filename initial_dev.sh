#!/bin/bash

# Create a virtual environment named 'venv'
python3 -m venv venv
if [ -d "venv" ]; then
    echo "venv already exists. run 'source venv/bin/activate'"
    exit 1
fi

# Initial Install the dependencies from requirements.txt
pip install -r requirements.txt

echo "venv set up and ready to use, run 'source venv/bin/activate'"