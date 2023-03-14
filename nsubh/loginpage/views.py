from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def loginpage(request):
    template = loader.get_template('loginpage.html')
    return HttpResponse(template.render())
