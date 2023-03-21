import datetime
import dbm
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from pymongo import MongoClient
from loginpage import views
from django.views.decorators.csrf import csrf_exempt

# Initializing Database
USERNAME = ''
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        year = request.POST.get('year', False)
        error = None

        # Checks if username or password are missing
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        # If no error, upload the info to mongoDB
        if error is None:
            logincollection = nsubh["Login"]
            USERNAME = username
            information = {
            "Username:": username,
            "Password": password,
            "Year": year,
            "Date Created": datetime.datetime.utcnow()
            }
            logininfo = logincollection.insert_one(information)
            print(nsubh.list_collection_names())
            return render(request, 'loginpage.html')


    return render(request, 'registrationpage.html')
