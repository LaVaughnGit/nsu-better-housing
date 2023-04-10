from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from loginpage.views import loginpage
client = MongoClient("mongodb://localhost:27017")
nsubh = client["NSUBH"]


@csrf_exempt
def reviewpage(request):
    context = {}
    if request.method == 'POST':
        roomnumber = request.POST.get('room', False)
        bed = request.POST.get('bed', False)
        context = {
            'username': "test",
            'nnumber': "12345678",
            'email': '123@nova.edu',
            'roomnumber': roomnumber,
            'bed': bed,
        }
    return render(request, 'reviewpage.html', context)
