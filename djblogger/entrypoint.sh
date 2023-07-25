#!/bin/sh
echo 'Running collectstatic'
python manage.py collectstatic --no-input --settings=djblogger.settings.production

echo 'Applying migrations'
python manage.py wait_for_db --settings=djblogger.settings
python manage.py migrate --settings=djblogger.settings

echo 'Runing server'
gunicorn --env DJANGO_SETTINGS_MODULE=djblogger.settings djblogger.wsgi:application --bind 0.0.0.0:$PORT

