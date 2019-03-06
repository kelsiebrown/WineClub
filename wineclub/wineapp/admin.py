from django.contrib import admin
from .models import WineType, Wine, WineReview, Winery, Event

# Register your models here.
admin.site.register(WineType)
admin.site.register(Wine)
admin.site.register(WineReview)
admin.site.register(Winery)
admin.site.register(Event)