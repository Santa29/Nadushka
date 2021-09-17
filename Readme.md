This site is written to upgrage local site from narod.ru. It can collect the data from pubmed and some other resources via their API to provide the list of all articles written by scientists from database.

This project may install by two ways.
1. Local installation.
a) Install python 3.8.5
b) Go to the directory and run "pip install requierements.txt"
c) Run postgresql with /proj/.env settings
d) Run "
        python manage.py migrate --noinput
        python manage.py initDB
        python manage.py scrape
        python manage.py runserver 0.0.0.0:8000
        "
e) Go to localhost:8000