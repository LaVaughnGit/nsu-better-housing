from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from loginpage.views import loginpage


def _get_db():
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    return client["NSUBH"]

# Load Mako. Check if any beds are occupied from database collection


def makoRS(request):
    context = {}
    loginpage.building = 'MAK'
    mkh = _get_db()[loginpage.building]
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

# Load Commons. Check if any beds are occupied from database collection


def commonsRS(request):
    context = {}
    loginpage.building = 'COM'
    mkh = _get_db()[loginpage.building]
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

# Load Leogoodwin. Check if any beds are occupied from database collection


def leogoodwinRS(request):
    context = {}
    loginpage.building = 'LGW'
    mkh = _get_db()[loginpage.building]
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

# Load Farquhar. Check if any beds are occupied from database collection


def farquharRS(request):
    context = {}
    loginpage.building = 'FAR'
    mkh = _get_db()[loginpage.building]
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

# Load Founders. Check if any beds are occupied from database collection


def foundersRS(request):
    context = {}
    loginpage.building = 'FOU'
    mkh = _get_db()[loginpage.building]
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

# Load Vettel. Check if any beds are occupied from database collection


def vettelRS(request):
    context = {}
    loginpage.building = 'VET'
    mkh = _get_db()[loginpage.building]
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

# Load CLC. Check if any beds are occupied from database collection


def clcRS(request):
    context = {}
    loginpage.building = 'CLC'
    mkh = _get_db()[loginpage.building]
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

# Load Rolling. Check if any beds are occupied from database collection


def rollingRS(request):
    context = {}
    loginpage.building = 'ROLL'
    mkh = _get_db()[loginpage.building]
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
