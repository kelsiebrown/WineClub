from django import forms
from .models import Event, WineReview

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=WineReview
        fields='__all__'

