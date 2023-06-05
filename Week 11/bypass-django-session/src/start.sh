#!/usr/bin/env sh

# Web application initialization
python3 manage.py collectstatic --clear --noinput
python3 manage.py migrate

/entrypoint.sh