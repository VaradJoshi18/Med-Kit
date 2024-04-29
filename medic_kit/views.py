from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from register.models import user,doc,pharma
from django.contrib.auth.hashers import make_password
from register.forms import RegisterForm,RegisterDocForm,RegisterPharmaForm
# from django.shortcuts import render, redirect, ,HttpResponse

from blogs.forms import *
from blogs.models import *
from django.core.paginator import Paginator
from news.forms import *
from news.models import *


def about(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request,'about.html')

# def news(request):
#     type= request.session.get('type')
#     if type == None:
#         return render(request,'index.html')
#     else:    
#         return render(request, 'news.html')

# def blog(request):
#     type= request.session.get('type')
#     if type == None:
#         return render(request,'index.html')
#     else:
#         return render(request, 'blog.html')

def buy(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'buy.html')

def client(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'client.html')

def contact(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'contact.html')

def feedback(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'feedback.html')

def doctors(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'doctors.html')

def index(request):
    type= request.session.get('type')
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'index.html')
    
def userProfile(request):
    context={}
    type= request.session.get('type')
    uname = request.session.get('username')
    context['username'] = uname
    
    data = user.objects.filter(username=uname)
    context['data'] = data
    
    # form : view and update:
    
    context['users'] = user.objects.filter(username=uname)
	# obj = get_object_or_404(user, username=uname)
    
    
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'user-profile.html',context)
    
def edituserProfile(request,id):
    context_3 = {}
    uname = request.session.get('username')
    context_3['username'] = uname
    
    data = user.objects.filter(username=uname)
    context_3['data'] = data
    
    obj = get_object_or_404(user, id=id)
    form = RegisterForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password1 = make_password(form.cleaned_data['password1'])
        request.session['username'] = form.cleaned_data['username']
        sign_up.save()
        return redirect("/userProfile/")
    
    context_3['form'] = form
    return render(request, "edit-user-profile.html",context_3)

def docProfile(request):
    context={}
    type= request.session.get('type')
    uname = request.session.get('username')
    context['username'] = uname
    
    # form : view and update:
    
    context['doc'] = doc.objects.filter(username=uname)
	# obj = get_object_or_404(user, username=uname)
    
    
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'doc-profile.html',context)
    
def editdocProfile(request,id):
    context_3 = {}
    obj = get_object_or_404(doc, id=id)
    form = RegisterDocForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password = make_password(form.cleaned_data['password'])
        request.session['username'] = form.cleaned_data['username']
        sign_up.save()
        return redirect("/docProfile/")
    
    context_3['form'] = form
    return render(request, "edit-doc-profile.html",context_3)

#====================================================================================
def pharmaProfile(request):
    context={}
    type= request.session.get('type')
    username = request.session.get('username')
    context['username'] = username
    
    # form : view and update:
    
    context['pharma'] = pharma.objects.filter(username=username)
	# obj = get_object_or_404(user, username=uname)
    
    
    if type == None:
        return render(request,'index.html')
    else:
        return render(request, 'pharma-profile.html',context)
    
def editpharmaProfile(request,id):
    # return render(request,"edit-pharma-profile.html")
    context_3 = {}
    obj = get_object_or_404(pharma, id=id)
    form = RegisterPharmaForm(request.POST or None,request.FILES, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password = make_password(form.cleaned_data['password'])
        request.session['username'] = form.cleaned_data['username']
        sign_up.save()
        return redirect("/pharmaProfile/")
    
    context_3['form'] = form
    return render(request, "edit-pharma-profile.html",context_3)



#View news user side
def viewNewss(request):
	context = {}
	context["news"] = news.objects.all()
	return render(request, "news.html", context)

#View Blogs user side
def viewBlogss(request):
    blogs = blog.objects.all()
    p = Paginator(blogs, 1)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context ={'page_obj': page_obj}
    return render(request,'blog.html',context)