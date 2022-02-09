from django.shortcuts import render
from .forms import *
# Create your views here.

def signin(request):

    return render(request, "signin.html")

def login(request):

    return render(request, "login.html")

def dashboard(request):
        
    return render(request, "dashboard.html")
