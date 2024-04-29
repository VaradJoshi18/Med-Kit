
import os
import re
import statistics
from tabnanny import check
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.views import LoginView #
from django.contrib.auth import authenticate, login
from django.conf import settings
from medic_kit.settings import PROJECT_ROOT
from ..models import user,doc,pharma
import io
import numpy as np
from PIL import Image
import face_recognition
# from django.shortcuts import 
# from ..forms import LoginUserForm 
from ..forms import LoginUserForm, LoginDocForm, LoginPharmaForm
import cv2
import base64
from django.core.files.base import ContentFile
from django.templatetags.static import static
def login_home(request):
    return render(request, "login-main.html")

def login_request(request):
    if request.method == 'POST':
        # form = LoginUserForm(request.POST)
        # if form.is_valid():
            username_got = request.POST['username']
            password = request.POST['password']
            obj = get_object_or_404(user, username=username_got)
            res = check_password(password,obj.password1)            #check_password is an hashing method
            
            if res == True:
                # login(request, username_got)
                context={}
                
                request.session['username']=request.POST['username']
                context['username'] = request.POST['username']
                request.session['type']=0
                # request.session['image'] = request.POST['image']
                messages.info(request, f"You are now logged in as {username_got}")
                return redirect('/index/')

         
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginUserForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html")

def login_doc_request(request):
    # template_name = "login.html"
    # form_class = LoginUserForm
    if request.method == 'POST':
        # form = LoginDocForm(request.POST)
        # # form = AuthenticationForm(request=request, data=request.POST)
        # if form.is_valid():
            username_got = request.POST['username']
            password = request.POST['password']
            
            #     # password = make_password(request.POST['password'])
            #     # return render(request, 'demo.html') #, {'access':check_password}
            
            obj = get_object_or_404(doc, username=username_got)
            res = check_password(password,obj.password)
            
            if res == True:
                request.session['type']=1
                request.session['username'] = request.POST['username']
                #request.session['type']=1
                # login(request, user_check)
                messages.info(request, f"You are now logged in as {username_got}")
                return HttpResponseRedirect('/index/')
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginDocForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html")

def login_pharma_request(request):
    # template_name = "login.html"
    # form_class = LoginUserForm
    if request.method == 'POST':
        form = LoginPharmaForm(request.POST)
        # form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username_got = request.POST['username']
            password = request.POST['password']
            
            #     # password = make_password(request.POST['password'])
            #     # return render(request, 'demo.html') #, {'access':check_password}
            
            obj = get_object_or_404(pharma, username=username_got)
            res = check_password(password,obj.password)
            
            if res == True:
                request.session['type']=2
                request.session['username'] = request.POST['username']
                messages.info(request, f"You are now logged in as {username_got}")
                return HttpResponseRedirect('/index/')
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginPharmaForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html")

def login_admin(request):
    if request.method == 'POST':
        # form = LoginUserForm(request.POST)
        # if form.is_valid():
            username_got = request.POST['username']
            password = request.POST['password']
            # obj = get_object_or_404(user, username=username_got)
            obj = get_object_or_404(user, username=username_got)
            res = check_password(password,obj.password1)    #check_password is an hashing method
            
            if res == True and obj.is_admin == 1:
                request.session['username']=request.POST['username']
                request.session['type']=3
                messages.info(request, f"You are now logged in as {username_got}")
                return redirect('/ad/home/')
            else:
                messages.error(request, "Invalid username or password.")
                
    else:
        form = LoginUserForm()
        # messages.error(request, "error 2.")
    # form = AuthenticationForm()
    return render(request, template_name = "login.html")

def logout(request):
    del request.session['type']
    del request.session['username']
    # except KeyError:
    #     pass
    return redirect('/index/')

# ============================PROFILES============================================================

def userprofile(request):
    return render(request, "user-profile.html")

def docprofile(request):
    return render(request, "doc-profile.html")

def pharmaprofile(request):
    return render(request, "pharma-profile.html")

# ======================================================================================================

def view_doctors(request):
    context = {}
    type = request.session.get('type')
    context['type'] = type
    context['data2'] = doc.objects.all()
    # context['username'] = username
    # context['data'] = user.objects.filter(username = username)
    username = request.session.get('username')
    context['username'] = username
    context['data'] = user.objects.filter(username = username)
    return render(request,'user-side-doctor-view.html', context)

# ========================================= Face Login ===================================================
def video(request):
    return render(request,'video.html')

def base64_file(request,data):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    name = 'Demo'
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

def base64_file_image(request):
    data=request.POST.get('dataimg')
    encoded_img = data.split(",")[1]
    # return HttpResponse(encoded_img)
    binary = base64.b64decode(encoded_img)
    
    image = np.asarray(bytearray(binary), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
   
    enterimage_encoding = face_recognition.face_encodings(image)[0]    #try
    users=user.objects.all()
    data=[]
    for u in users:
        module_dir = os.path.dirname(__file__)
        sub=u.image.url.split('/')
        x = module_dir.replace("views", "imgaes")
        x=x+"\\"+sub[3]
        mg=cv2.imread(x,cv2.IMREAD_COLOR)
        dbenterimage_encoding = face_recognition.face_encodings(mg)[0]  #try
        dbresults = face_recognition.compare_faces([enterimage_encoding], dbenterimage_encoding) 
     
        if dbresults[0]:
            request.session['username']=u.username
            request.session['type']=0
            messages.info(request, f"You are now logged in as {u.username}")
            return redirect('/index/')
            
        
       
    return HttpResponse("No user found")
     