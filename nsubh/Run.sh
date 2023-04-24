#!/bin/sh

python -m pip install pymongo

mongoimport --db NSUBH --collection MAK < ../NSUBH/datasets/MAK.json --jsonArray
echo "File added."
echo "Welcome to NSUBH!"

python manage.py runserver
chmod +x Run.sh
