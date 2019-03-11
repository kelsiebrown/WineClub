from django.shortcuts import render, get_object_or_404
from .models import Wine, Winery, WineType, Event, WineReview
from .forms import EventForm, ReviewForm
from django.contrib.auth.decorators import login_required

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

def reviews(request):
    review_list = WineReview.objects.all()
    return render(request, 'wineapp/reviews.html', {'review_list': review_list})

def winedetail (request, id):
    detail = get_object_or_404(Wine, pk=id)
    context = {'detail': detail}
    return render (request, 'wineapp/details.html', context=context)

# form views
@login_required
def newEvent(request):
    form=EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'wineapp/newevent.html', {'form': form})

def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'wineapp/newreview.html', {'form': form})

#login/logout functionality
def loginmessage(request):
    return render(request, 'wineapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'wineapp/logoutmessage.html')

