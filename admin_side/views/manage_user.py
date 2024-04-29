import csv
from django.http import HttpResponseRedirect
from register.models import user
from register.forms import *
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.hashers import make_password

def viewUser(request):
    context = {}
    
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["users"] = user.objects.all()
    return render(request, "user-view.html", context)

def addUser(request):
	context_1 = {}
	form = RegisterForm(request.POST or None)
	
	if form.is_valid():
            # return HttpResponseRedirect('hi')
			sign_up = form.save(commit=False)
			sign_up.password1 = make_password(form.cleaned_data['password1'])
			sign_up.save()
			
			form.save()
			return redirect("/ad/viewUser/")

	context_1['form'] = form
	return render(request, "userAdd.html",context_1)

def deleteUser(request,username):
	# context_2={}
	obj = get_object_or_404(user, username=username)
	if request.method == "GET":
		obj.delete()
		return redirect("/ad/viewUser/")
	return render(request, "user-view.html")

def editUser(request,id):
    context_3 = {}
    obj = get_object_or_404(user, id=id)
    form = RegisterForm(request.POST or None, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password1 = make_password(form.cleaned_data['password1'])
        sign_up.save()
        return redirect("/ad/viewUser/")
    
    context_3['form'] = form
    return render(request, "UserAdd.html",context_3)


def download_user_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=patients.csv'
	writer = csv.writer(response)
    # fields = ['first_name', 'last_name', 'username', 'email', 'address', 'password1']

	writer.writerow(['First Name','Last Name','User Name','Email','Address','Password'])
	for data in user.objects.all():
		writer.writerow([data.first_name,data.last_name,data.username,data.email,data.address,data.password1,])

	return response