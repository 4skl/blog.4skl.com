#!/bin/sh

# Migrate the database
python manage.py migrate

# Load the initial data
python manage.py loaddata fixtures/initial_data.json

# Run the Gunicorn server
gunicorn skl_backend.wsgi --bind 0.0.0.0:8000 --log-level=debug