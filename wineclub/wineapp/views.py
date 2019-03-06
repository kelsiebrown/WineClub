from django.shortcuts import render
from .models import Wine, Winery, WineType, Event

# Create your views here.

def index(request):
    return render(request, 'wineapp/index.html')

def winetypes (request):
    winetype_list=WineType.objects.all()
    return render (request, 'wineapp/winetypes.html', {'winetype_list':winetype_list})

def wines(request):
    wine_list = Wine.objects.all()
    return render(request, 'wineapp/wines.html', {'wine_list': wine_list})

def wineries(request):
    winery_list = Winery.objects.all()
    return render(request, 'wineapp/wineries.html', {'winery_list': winery_list})

def events(request):
    event_list = Event.objects.all()
    return render(request, 'wineapp/events.html', {'event_list': event_list})
