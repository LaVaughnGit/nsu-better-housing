import datetime
import dbm
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from pymongo import MongoClient

# Initializing Database
USERNAME = ''
client = MongoClient('mongodb://localhost:27017')
NSUBH = client['NSUBH']


def register(request):
    registerPage = loader.get_template('registrationpage.html')
    if request.method == 'POST':
        username = request.form['usernmae']
        password = request.form['password']
        year = request.form['year']
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                logincollection = NSUBH['Login']
                USERNAME = username
                information = {
                    "Username:": username,
                    "Password": password,
                    "Year": year,
                    "Date Created": datetime.datetime.utcnow
                }
                document = logincollection.insert_one(information).inserted_id
            except dbm.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect('/loginpage/')

    return HttpResponse(registerPage.render())
