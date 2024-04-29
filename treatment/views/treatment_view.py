import csv
from ..forms import *
from ..models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from register.models import user

import logging
logger = logging.getLogger(__name__)



def viewTreatment(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    context["treatment"] = treatment.objects.all()
    return render(request, "treatmentview.html", context)

def addTreatment(request):
	context = {}
	form = RegisterTreatForm(request.POST)

	if form.is_valid():
			
			form.save()
			logger.info("Treatment was added")
			return redirect("/treatment/treatView/")

	context['form'] = form
	return render(request, "treatmentAdd.html",context)

def deleteTreatment(request,id):
	context={}
	obj = get_object_or_404(treatment, id=id)#
	if request.method == "GET":
		obj.delete()
		logger.info("Treatment was Deleted")

		return redirect("/treatment/treatView/")
	return render(request, "treatmentview.html", context)

def editTreatment(request,id):
    context = {}
    obj = get_object_or_404(treatment, id=id)
    form = RegisterTreatForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
		
        return redirect("/treatment/treatView/")
    
    context['form'] = form
    return render(request, "treatmentAdd.html",context)

def download_treatment_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=treatment.csv'
	writer = csv.writer(response)
	writer.writerow(['Ref Id','Remedy 1','Remedy 2','Remedy 3'])
	for data in treatment.objects.all():
		writer.writerow([data.idd,data.remedies_1,data.remedies_2,data.remedies_3])

	return response