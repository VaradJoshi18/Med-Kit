# from http.client import HTTPResponse
import csv
from django.http import HttpResponseRedirect
from register.models import doc
from register.forms import *
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.hashers import make_password



import logging
logger = logging.getLogger(__name__)



def viewPharma(request):
    context = {}
    
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["pharmacists"] = pharma.objects.all()
    return render(request, "pharma-view.html", context)

def addPharma(request):
	context_1 = {}
	form = RegisterPharmaForm(request.POST or None)
	
	if form.is_valid():
            # return HttpResponseRedirect('hi')
			sign_up = form.save(commit=False)
			sign_up.password = make_password(form.cleaned_data['password'])
			sign_up.save()
			
			form.save()
			return redirect("/ad/viewPharma/")

	context_1['form'] = form
	return render(request, "pharmaAdd.html",context_1)

def deletePharma(request,username):
	context_2={}
	obj = get_object_or_404(pharma, username=username)
	if request.method == "GET":
		obj.delete()
		return redirect("/ad/viewPharma/")
	return render(request, "pharma-view.html", context_2)

def editPharma(request,id):
    context_3 = {}
    obj = get_object_or_404(pharma, id=id)
    form = RegisterPharmaForm(request.POST or None, instance=obj)
    if form.is_valid():
        sign_up = form.save(commit=False)
        sign_up.password = make_password(form.cleaned_data['password'])
        sign_up.save()
        return redirect("/ad/viewPharma/")
    
    context_3['form'] = form
    return render(request, "PharmaAdd.html",context_3)



def download_pharma_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=pharmacist.csv'
	writer = csv.writer(response)
    # fields = ('name', 'shopName', 'shopAddr', 'licenseNumber', 'city', 'nationwideDel', 'username', 'password', 'email')

	writer.writerow(['Name','Shop Name','Shop Address','License Number','City','NationalWideDelivery','username','Password','email'])
	for data in pharma.objects.all():
		writer.writerow([data.name,data.shopName,data.shopAddr,data.licenseNumber,data.city,data.nationwideDel,data.username,data.password,data.email])

	return response