from django.shortcuts import render
from .forms import *
# Create your views here.

def sigin(request):

    return render(request, "sigin.html")

def simulator(request):

    if request.method == 'POST':
        form = schedule(request.POST, label_suffix='')
        if form.is_valid():
            selection = form.cleaned_data.get('selection')
            # do something with your results
            print(selection)
    else:
        form = schedule

        
    return render(request, "simulator.html", {'form': form})
