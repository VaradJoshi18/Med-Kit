from django import forms
from .models import *

class RegisterMedicineForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields="__all__"