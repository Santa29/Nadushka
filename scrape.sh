#!/bin/bash

cd /var/app
export PYTHONPATH=/var/app;$PYTHONPATH

python manage.py scrape
python manage.py runserver 0.0.0.0:8080