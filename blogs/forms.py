from dataclasses import field
from django import forms
from .models import *
 
class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields="__all__"