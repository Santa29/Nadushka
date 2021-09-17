#!/bin/bash

cd /usr/src/Nadushka/
export PYTHONPATH=/usr/src/Nadushka;$PYTHONPATH

python manage.py migrate --noinput
python manage.py initDB
python manage.py scrape
python manage.py runserver 0.0.0.0:8000