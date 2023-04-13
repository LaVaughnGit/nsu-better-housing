from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from loginpage.views import userNameStored, nNumberStored
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
        print(userNameStored)
        print(nNumberStored)
        context = {
            'username': userNameStored,
            'nnumber': nNumberStored,
            'email': '123@nova.edu',
            'roomnumber': roomnumber,
            'bed': bed,
        }
    return render(request, 'reviewpage.html', context)
