from django.shortcuts import render,get_object_or_404,redirect
from register.models import user
from register.forms import RegisterForm
from django.contrib.auth.hashers import make_password

def index(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    return render(request, "home.html",context)