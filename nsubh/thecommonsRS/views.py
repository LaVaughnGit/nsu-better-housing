from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def commonsRS(request):
    template = loader.get_template('commonsRS.html')
    return HttpResponse(template.render())
