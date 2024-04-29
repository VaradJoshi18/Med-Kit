from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #
from .models import *

# class AppointmentForm(forms.ModelForm):
# # not null field define karna
#     class Meta:
#         model = Appointment
#         fields = ['fname','lname','email','address','time','day','request','status','username']

class UserAppointmentForm(forms.ModelForm):
# not null field define karna
    class Meta:
        model = Appointment
        fields = ['fname','lname','email','time','day','request','username']

# 'fname','lname','email','address','time','day','request','status'


class AcceptAppointmentForm(forms.ModelForm):
# not null field define karna
   class Meta:
       model = Appointment
       fields = '__all__'