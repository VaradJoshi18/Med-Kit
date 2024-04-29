from dataclasses import field
from django import forms
from .models import *
 
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields="__all__"