from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())
