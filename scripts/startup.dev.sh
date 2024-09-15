#!/bin/bash

poetry run python manage.py migrate
python manage.py collectstatic --no-input
poetry run python manage.py runserver 0.0.0.0:8000
