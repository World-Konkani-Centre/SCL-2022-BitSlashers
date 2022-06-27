from decimal import Context
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
