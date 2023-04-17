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
        roomnumber = request.POST.get('R', False)
        bed = request.POST.get('B', False)
        print(roomnumber)
        print(bed)
        print(loginpage.user)
        print(loginpage.password)
        reviewpage.roomnumber = roomnumber
        reviewpage.bed = bed
        context = {
            'username': loginpage.firstname + " " + loginpage.lastname,
            'nnumber': loginpage.nnumber,
            'email': loginpage.email,
            'roomnumber': roomnumber,
            'bed': bed,
        }
    return render(request, 'reviewpage.html', context)
