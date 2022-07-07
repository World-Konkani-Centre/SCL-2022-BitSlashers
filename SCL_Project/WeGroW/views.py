from decimal import Context
from django.shortcuts import redirect, render

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout



def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def sample(request):
    return render(request, 'sample-inner-page.html')

def service(request):
    return render(request, 'services.html')

def service_detail(request):
    return render(request, 'service-details.html')

def add_store(request):
    return render(request, 'create_store.html')

def my_logout(request):
    logout(request)
    return redirect('login')


