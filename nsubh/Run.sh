#!/bin/sh

python -m pip install pymongo
python manage.py runserver
chmod +x Run.sh
echo "Welcome to NSUBH!"