import csv
from django.http import HttpResponse
from ..forms import *
from ..models import *
from register.models import *

from django.shortcuts import render, redirect, get_object_or_404

import logging
logger = logging.getLogger(__name__)

def viewDisease(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username="Admin")
    context['data'] = data
    context["disease"] = disease.objects.all()
    return render(request, "diseaseview.html", context)

def addDisease(request):
	context = {}
	form = RegisterDisForm(request.POST)

	if form.is_valid():
			
			form.save()
			logger.info("Diesease was added")
			return redirect("/ill/diseaseView/")

	context['form'] = form
	return render(request, "diseaseAdd.html",context)

def deleteDisease(request,id):
	context={}
	obj = get_object_or_404(disease, id=id)#
	if request.method == "GET":
		obj.delete()
		logger.info("Disease was Deleted")
		return redirect("/ill/diseaseView/")
	return render(request, "diseaseview.html", context)

def editDisease(request,id):
    context = {}
    obj = get_object_or_404(disease, id=id)
    form = RegisterDisForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
		
        return redirect("/ill/diseaseView/")
    
    context['form'] = form
    return render(request, "diseaseAdd.html",context)

def bulk_upload(request):
	return render(request,"bulkUpload.html")

def upload_csv(request):
	if request.method == 'GET':
		return render(request, "bulkUpload.html")
		
		# return HttpResponse("Not Valid method")
		
	csv_file=request.FILES['csv_file']
	if not csv_file.name.endswith('.csv'):
		return HttpResponse("File not valid")
	if csv_file.multiple_chunks():
		return HttpResponse("Uploaded file is big")
		
	file_data = csv_file.read().decode("UTF-8")
	lines = file_data.split("\n")
	c = len(lines)
	#return HttpResponse(lines[0])
	for i in range(0,c-1):
		fields = lines[i].split(",")
		data_dict = {}
		data_dict["name"] = fields[0]
		data_dict["symptom_1"]=fields[1]
		data_dict["symptom_2"]=fields[2]
		data_dict["symptom_3"]=fields[3]
		#return HttpResponse(fields[1])
		cform=RegisterDisForm(data_dict)
		if cform.is_valid():
			cform.save()
			
	return redirect("/ill/diseaseView/")
def download_disease_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=disease.csv'
	writer = csv.writer(response)
	writer.writerow(['Name','Symptom 1','Symptom 2','Symptom 3',])
	for data in disease.objects.all():
		writer.writerow([data.name,data.symptom_1,data.symptom_2,data.symptom_3])

	return response