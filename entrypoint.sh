#!/bin/sh

python manage.py makemigrations website --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn website.wsgi:application --bind 0.0.0.0:8000