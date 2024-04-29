from django import forms
from .models import *

class RegisterPrescriptionForm(forms.ModelForm):
    class Meta:
        model = prescription
        fields="__all__"