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
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'makors.html', context)


def commonsRS(request):
    context = {}
    loginpage.building = 'COM'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'commonsrs.html', context)


def leogoodwinRS(request):
    context = {}
    loginpage.building = 'LGW'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'leogoodwinrs.html', context)


def farquharRS(request):
    context = {}
    loginpage.building = 'FAR'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'farquharrs.html', context)


def foundersRS(request):
    context = {}
    loginpage.building = 'FOU'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'foundersrs.html', context)


def vettelRS(request):
    context = {}
    loginpage.building = 'VET'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'vettelrs.html', context)


def clcRS(request):
    context = {}
    loginpage.building = 'CLC'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'clcrs.html', context)


def rollingRS(request):
    context = {}
    loginpage.building = 'ROLL'
    mkh = nsubh[loginpage.building]
    cursor = mkh.find({})
    occupiedBeds = []
    for document in cursor:
        roomNumber = document['Room']
        bedType = document['Bed']
        if document['Occupied'] == 'T':
            occupiedBeds.append(roomNumber + "" + bedType)
    context = {
        "occupiedrooms": occupiedBeds,
        "firstname": loginpage.firstname,
        "lastname": loginpage.lastname,
        "nnumber": loginpage.nnumber,
    }
    return render(request, 'rollingrs.html', context)
