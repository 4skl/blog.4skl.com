#!/bin/sh

# Migrate the database
python manage.py migrate --settings=skl_backend.settings_dev

# Load the initial data
python manage.py loaddata fixtures/initial_data.json --settings=skl_backend.settings_dev

# Run the Django development server
python manage.py runserver --settings=skl_backend.settings_dev 0.0.0.0:8000