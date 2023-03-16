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
        print('WORKING')
        username = request.POST['username']
        password = request.POST['password']
        year = request.POST.get('year', False)
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if error is None:
            try:
                # print('working')
                logincollection = nsubh["Login"]
                USERNAME = username
                print(f"{username}, {password}, {year}")
                information = {
                    "Username:": username,
                    "Password": password,
                    "Year": year,
                    "Date Created": datetime.datetime.utcnow()
                }
                print('working')
                logininfo = logincollection.insert_one(information)
                print(logininfo.inserted_id)
                print(nsubh.list_collection_names())
            except Exception:
                print(Exception)
            else:
                return render(request, 'registrationpage.html')

    return render(request, 'registrationpage.html')
