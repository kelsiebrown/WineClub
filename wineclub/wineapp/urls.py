from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('winetypes/', views.winetypes, name='winetypes'),
    path('wines/', views.wines, name='wines'),
    path('wineries/', views.wineries, name='wineries'),
    path('events/', views.events, name='events'),
    path('reviews/', views.reviews, name='reviews'),
    path('winedetail/<int:id>', views.winedetail, name='details'),
    path('newEvent', views.newEvent, name='newevent'),
    path('newReview', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]