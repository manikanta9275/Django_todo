#!/bin/bash

# Install pip if it's not available
if ! command -v pip &> /dev/null
then
    echo "pip not found, installing..."
    apt-get update && apt-get install -y python3-pip
fi

# Install dependencies
pip install -r requirements.txt

# Run Django collectstatic to handle static files
python manage.py collectstatic --noinput
