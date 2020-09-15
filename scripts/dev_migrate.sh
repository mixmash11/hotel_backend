#!/bin/bash
#### Description: makes migrations and executes them on the dev compose instance
docker-compose -f ../local.yml run --rm django python manage.py makemigrations
docker-compose -f ../local.yml run --rm django python manage.py migrate
./fix_permissions.sh
