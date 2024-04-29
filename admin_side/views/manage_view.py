import csv
from django.http import HttpResponse
from register.models import doc
from register.forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password

def index_manage(req):
    return render(req, "login.html")

def viewDoc(request):
    context = {}
    
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["doctor"] = doc.objects.all()
    return render(request, "doc-view.html", context)

def addDoc(request):
	context = {}
	form = RegisterDocForm(request.POST)

	if form.is_valid():
			sign_up = form.save(commit=False)
			sign_up.password = make_password(form.cleaned_data['password'])
			sign_up.save()
			return redirect("/ad/viewDoc")

	context['form'] = form
	return render(request, "docAdd.html",context)

def deleteDoc(request,id):
	context={}
	obj = get_object_or_404(doc, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/ad/viewDoc/")
	return render(request, "doc-view.html", context)

def editDoc(request,id):
    context = {}
    obj = get_object_or_404(doc, id=id)
    form = RegisterDocForm(request.POST or None, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password = make_password(form.cleaned_data['password'])
        sign_up.save()
        return redirect("/ad/viewDoc/")
    
    context['form'] = form
    return render(request, "docAdd.html",context)


def download_doc_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=doctors.csv'
	writer = csv.writer(response)
	        # fields = ['name', 'age', 'experience', 'hosName', 'hosLocation', 'email', 'degree', 'phone', 'username','password']

	writer.writerow(['Name','Age','Experience','Hospital Name','Hospital Location','Email','Degree','Phone','Username','Password'])
	for data in doc.objects.all():
		writer.writerow([data.name,data.age,data.experience,data.hosName,data.hosLocation,data.email,data.degree,data.phone,data.username,data.password])

	return response