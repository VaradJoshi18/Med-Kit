from dataclasses import field
from django import forms
from .models import *
 
class NewsForm(forms.ModelForm):
    class Meta:
        model = news
        fields="__all__"