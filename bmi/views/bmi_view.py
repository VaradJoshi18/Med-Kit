from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import bmi, ideal_bmi
from ..forms import bmiForm, bmiIdealForm
from register.models import user
import csv
from django.db.models import Q

import logging
logger = logging.getLogger(__name__)


#===================================USER===========================================

def viewbmi(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["bmi"] = bmi.objects.all()
    return render(request, "bmi-view.html", context)

def addbmi(request):
	context = {}
	form = bmiForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
		form.save()
		logger.info("BMI was added")
		return redirect("/bmi/viewbmi/")

	context['form'] = form
	return render(request, "bmiAdd.html",context)

def deletebmi(request,id):
	context={}
	obj = get_object_or_404(bmi, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/bmi/viewbmi/")
	return render(request, "bmi-view.html", context)

def editbmi(request,id):
    context = {}    
    obj = get_object_or_404(bmi, id=id)
   
    form = bmiForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
		
        return redirect("/bmi/viewbmi/")
    
    context['form'] = form
    return render(request, "bmiAdd.html",context)

#===================================IDEAL===========================================

def viewidealbmi(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["ideal_bmi"] = ideal_bmi.objects.all()
    return render(request, "idealBmi-view.html", context)

def addidealbmi(request):
	context = {}
	form = bmiIdealForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
	if form.is_valid():
		form.save()
		return redirect("/bmi/viewidealbmi/")

	context['form'] = form
	return render(request, "idealBmiAdd.html",context)

def deleteidealbmi(request,id):
	context={}
	obj = get_object_or_404(ideal_bmi, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/bmi/viewidealbmi/")
	return render(request, "idealBmi-view.html", context)

def editidealbmi(request,id):
    context = {}    
    obj = get_object_or_404(ideal_bmi, id=id)
   
    form = bmiIdealForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/bmi/viewidealbmi/")
    
    context['form'] = form
    return render(request, "idealBmiAdd.html",context)

def download_bmi_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=BMI.csv'
	writer = csv.writer(response)
	writer.writerow(['ID','Age','Gender','User Weight','User hieght','User BMI'])
	for data in bmi.objects.all():
		writer.writerow([data.userId,data.age,data.gender,data.user_weight,data.user_height,data.user_bmi])

	return response

def download_ideal_bmi_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=Ideal_BMI.csv'
	writer = csv.writer(response)
	writer.writerow(['age_range','gender','ideal_weight','ideal_height','ideal_bmi'])
	for data in ideal_bmi.objects.all():
		writer.writerow([data.age_range,data.gender,data.ideal_weight,data.ideal_height,data.ideal_bmi])

	return response

# ===========================USER SIDE=======================================================

def user_bmi_view(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    
    data = user.objects.filter(username=username)
    context['data'] = data
    
    user_bmi = bmi.objects.filter(userId = username)
    context['user_bmi'] = user_bmi
    
    user_bmi_temp = bmi.objects.filter(userId = username).values_list('age')
    # return HttpResponse(user_bmi_temp)
    # age = user_bmi[1]
    
    # user_ideal_bmi = ideal_bmi.objects.filter(Q(age_range__bte =user_bmi_temp))
    # context['user_ideal_bmi'] = user_ideal_bmi
    
    return render(request,"user-bmi-view.html",context)