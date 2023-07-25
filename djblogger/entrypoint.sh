#!/bin/sh
echo 'Running collectstatic'
python manage.py collectstatic --no-input --settings=djblogger.settings.production

echo 'Applying migrations'
python manage.py wait_for_db --settings=config.settings.production
python manage.py makemigrations --settings=djblogger.settings.production
python manage.py migrate --settings=djblogger.settings.production

echo 'Runing server'
gunicorn --env DJANGO_SETTINGS_MODULE=djblogger.settings.production djblogger.wsgi:application --bind 0.0.0.0:$PORT

