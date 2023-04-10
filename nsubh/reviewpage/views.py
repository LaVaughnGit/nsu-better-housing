from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reviewpage(request):
    context = {}
    if request.method == 'GET':

        context = {
            'username': 'testing',
            'nnumber': '12345678',
            'email': '123@nova.edu',
        }
    return render(request, 'reviewpage.html', context)
