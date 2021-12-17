from django.shortcuts import render

# Create your views here.

def simulator(request):

    return render(request, "simulator.html")