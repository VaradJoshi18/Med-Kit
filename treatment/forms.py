from django import forms
from .models import *

class RegisterTreatForm(forms.ModelForm):
    class Meta:
        model = treatment
        fields="__all__"