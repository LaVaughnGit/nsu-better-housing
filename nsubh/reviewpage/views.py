from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reviewpage(request):
    template = loader.get_template('reviewpage.html')
    return HttpResponse(template.render())
