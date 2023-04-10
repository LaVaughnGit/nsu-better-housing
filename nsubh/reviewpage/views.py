from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reviewpage(request):
    if request.method == 'POST':
        context = {
            'username': 'testing',
            'nnumber': '12345678',
        }
    return render(request, 'reviewpage.html', context)
