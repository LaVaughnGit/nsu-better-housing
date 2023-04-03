from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def makofs(request):
    template = loader.get_template('makoFS.html')
    return HttpResponse(template.render())

def commonsFS(request):
    template = loader.get_template('commonsFS.html')
    return HttpResponse(template.render())

def leogoodwinFS(request):
    template = loader.get_template('leogoodwinFS.html')
    return HttpResponse(template.render())

def farquharFS(request):
    template = loader.get_template('farquharFS.html')
    return HttpResponse(template.render())

def foundersFS(request):
    template = loader.get_template('foundersFS.html')
    return HttpResponse(template.render())

def vettelFS(request):
    template = loader.get_template('vettelFS.html')
    return HttpResponse(template.render())

def clcFS(request):
    template = loader.get_template('clcFS.html')
    return HttpResponse(template.render())

def rollingFS(request):
    template = loader.get_template('rollingFS.html')
    return HttpResponse(template.render())