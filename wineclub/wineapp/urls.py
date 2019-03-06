from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('winetypes/', views.winetypes, name='winetypes'),
    path('wines/', views.wines, name='wines'),
    path('wineries/', views.wineries, name='wineries'),
    path('events/', views.events, name='events'),
]