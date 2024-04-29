from .models import *
from django import forms

class chatForm(forms.ModelForm):
    class Meta:
        model = chat
        fields="__all__"