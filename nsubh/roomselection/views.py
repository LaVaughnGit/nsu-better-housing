from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pymongo import MongoClient
import loginpage.views
# Create your views here.
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]


def makoRS(request):
    template = loader.get_template('makoRS.html')
    mkh = nsubh['MKH']
    cursor = mkh.find({})
    for document in cursor:
        if document['Occupied'] == 'T':
            print('LFG')
    return HttpResponse(template.render())


def commonsRS(request):
    template = loader.get_template('commonsRS.html')
    return HttpResponse(template.render())


def leogoodwinRS(request):
    template = loader.get_template('leogoodwinRS.html')
    return HttpResponse(template.render())


def farquharRS(request):
    template = loader.get_template('farquharRS.html')
    return HttpResponse(template.render())


def foundersRS(request):
    template = loader.get_template('foundersRS.html')
    return HttpResponse(template.render())


def vettelRS(request):
    template = loader.get_template('vettelRS.html')
    return HttpResponse(template.render())


def clcRS(request):
    template = loader.get_template('clcRS.html')
    return HttpResponse(template.render())


def rollingRS(request):
    template = loader.get_template('rollingRS.html')
    return HttpResponse(template.render())
