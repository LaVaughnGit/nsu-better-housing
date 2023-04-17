from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pymongo import MongoClient
from loginpage.views import loginpage
# Create your views here.
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]


def makoRS(request):
    context = {}
    loginpage.building = 'MAK'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
    }
    return render(request, 'makors.html', context)


def commonsRS(request):
    template = loader.get_template('commonsRS.html')
    loginpage.building = 'COM'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
    return HttpResponse(template.render())


def leogoodwinRS(request):
    template = loader.get_template('leogoodwinRS.html')
    loginpage.building = 'LGW'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
    return HttpResponse(template.render())


def farquharRS(request):
    template = loader.get_template('farquharRS.html')
    loginpage.building = 'FAR'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
            occupiedBeds.append(roomNumber + "" + bedType)
    return HttpResponse(template.render())


def foundersRS(request):
    template = loader.get_template('foundersRS.html')
    loginpage.building = 'FOU'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
    return HttpResponse(template.render())


def vettelRS(request):
    template = loader.get_template('vettelRS.html')
    loginpage.building = 'VET'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
    return HttpResponse(template.render())


def clcRS(request):
    template = loader.get_template('clcRS.html')
    loginpage.building = 'CLC'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
    return HttpResponse(template.render())


def rollingRS(request):
    template = loader.get_template('rollingRS.html')
    loginpage.building = 'ROLL'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            print(roomNumber + '' + bedType)
    return HttpResponse(template.render())
