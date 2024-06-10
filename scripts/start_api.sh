#!/usr/bin/bash

set -o errexit
set -o nounset

# Check env variables
echo "DJANGO_ENV is ${DJANGO_ENV}"
echo "Port ${DJANGO_PORT} exposed for Libro Smart API"

# Set working directory
cd ${PROJECT_DIR}
echo "Change to working directory $(pwd)"

## Run database migrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py init_admin


if [ ${DJANGO_ENV} = 'development' ]; then
    python manage.py runserver 0.0.0.0:${DJANGO_PORT}
else
   gunicorn src.config.wsgi:application --bind 0.0.0.0:${DJANGO_PORT} --workers 4 --threads 4
fi