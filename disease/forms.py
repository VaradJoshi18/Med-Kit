from django import forms
from .models import *

class RegisterDisForm(forms.ModelForm):
    class Meta:
        model = disease
        fields="__all__"