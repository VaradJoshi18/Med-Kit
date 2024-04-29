from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
# from django.contrib.auth.views import LoginView #
# from ..forms import RegisterForm, LoginForm #


import logging
logger = logging.getLogger(__name__)


from ..forms import *

def reg_home(request):
    return render(request, "reg.html")

class MainView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'main.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/index/')

        return render(request, self.template_name, {'form': form})

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password1 = make_password(form.cleaned_data['password1'])
            sign_up.status = 1
            sign_up.save()
            logger.info("User Was Registered")

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/index/')

        return render(request, self.template_name, {'form': form})
    
class RegisterDocView(View):
    form_class = RegisterDocForm
    initial = {'key': 'value'}
    template_name = 'register-doc.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data['password'])
            sign_up.status = 1
            sign_up.save()
            logger.info("Doctor was Registered")
            # form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/index/')

        return render(request, self.template_name, {'form': form})
    
class RegisterPharmaView(View):
    form_class = RegisterPharmaForm
    initial = {'key': 'value'}
    template_name = 'register-pharma.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        # return HttpResponse(form)
        if form.is_valid():
            sign_up = form.save(commit=False)
            sign_up.password = make_password(form.cleaned_data['password'])
            sign_up.status = 1
            sign_up.save()
            logger.info("Pharmacist Was Registered")
            # form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/index/')

        return render(request, self.template_name, {'form': form})