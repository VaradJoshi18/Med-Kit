from django import forms

import medhistory
from .models import *

class RegisterMedhistoryForm(forms.ModelForm):
    class Meta:
        model = medhistory
        fields="__all__"