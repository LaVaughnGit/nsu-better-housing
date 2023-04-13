from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from homepage import views

client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]

userNameStored = ''
nNumberStored = ''


@csrf_exempt
def loginpage(request):
    # Check the request method

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        error = None
        docUser = None

        logincollection = nsubh['Login']
        userquery = {"Username": username}
        dbUserDocument = logincollection.find_one(userquery)
        if dbUserDocument:
            docUser = dbUserDocument["Username"]
            docPass = dbUserDocument["Password"]
            docNNumber = dbUserDocument["N Number"]

        user = docUser
        passwordChecker = False
        if user != username:
            error = 'Incorrect username.'

        elif docPass == password:
            passwordChecker = True

        elif not passwordChecker:
            error = 'Incorrect password.'
        else:
            error = None

        if error is None:
            userNameStored = docUser
            nNumberStored = docNNumber
            loginInformation = {
                'username': username,
                'nnumber': docNNumber,
            }
            return render(request, 'homepage.html', loginInformation)
        else:
            print(error)
            return render(request, 'loginpage.html')

    return render(request, 'loginpage.html')
