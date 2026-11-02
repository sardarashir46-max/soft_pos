
from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')


def starter_page(request):
    return render(request, 'home/starter.html')
