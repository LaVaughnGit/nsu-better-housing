from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from reviewpage.views import reviewpage
from loginpage.views import loginpage
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]


@csrf_exempt
def completionpage(request):
    if request.method == 'POST':
        logincollection = nsubh['MKH']
        userquery = {"Bed": reviewpage.bed, "Room": reviewpage.roomnumber}
        dbUserDocument = logincollection.find_one(userquery)
        updatedName = {
            '$set': {"Name": loginpage.firstname + " " + loginpage.lastname}}
        updatedStatus = {'$set': {"Occupied": "T"}}
        if dbUserDocument:
            logincollection.update_one(userquery, updatedName)
            logincollection.update_one(userquery, updatedStatus)
    return render(request, 'completionpage.html')
