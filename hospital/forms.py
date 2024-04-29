from dataclasses import field
from django import forms
from .models import *
 
class hospitalForm(forms.ModelForm):
    class Meta:
        model = hos
        fields="__all__"