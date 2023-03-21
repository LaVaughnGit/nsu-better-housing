from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient


@csrf_exempt
def loginpage(request):
    # Check the request method
        
    return render(request, 'loginpage.html')
