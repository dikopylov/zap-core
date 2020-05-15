#!/bin/sh

printf "===================Start database migrations===================\n"
python3 manage.py migrate
printf "===================Finish database migrations===================\n"
printf "===================Start server===================\n"
python3 manage.py runserver 0.0.0.0:8000