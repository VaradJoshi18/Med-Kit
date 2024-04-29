from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #
from .models import *

class ContactForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = contact
        fields = '__all__'