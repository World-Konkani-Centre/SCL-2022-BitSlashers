from decimal import Context
from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def store(request):
    return render(request, 'pricing.html')
