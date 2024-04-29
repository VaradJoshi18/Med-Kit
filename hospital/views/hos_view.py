import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from register.models import *
from ..forms import *
from ..models import *


import logging
logger = logging.getLogger(__name__)


def viewhos(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["hos"] = hos.objects.all()
    return render(request, "hos-view.html", context)

def addhos(request):
    context = {}
    form = hospitalForm(request.POST or None)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("Hospital Information was added")
        return redirect("/hospital/viewHos/")

    context['form'] = form
    return render(request, "hosAdd.html",context)

def deletehos(request,id):
	context={}
	obj = get_object_or_404(hos, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/hospital/viewHos/")
	return render(request, "hos-view.html", context)

def edithos(request,id):
    context = {}    
    obj = get_object_or_404(hos, id=id)
   
    form = hospitalForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        logger.info("Hospital Information was Edited")
        return redirect("/hospital/viewHos/")
    
    context['form'] = form
    return render(request, "hosAdd.html",context)

def bulk_upload2(request):
	return render(request,"bulkUpload2.html")

def upload_csv2(request):
	if request.method == 'GET':
		return render(request, "bulkUpload2.html")
		
		# return HttpResponse("Not Valid method")
		
	csv_file=request.FILES['csv_file2']
	if not csv_file.name.endswith('.csv'):
		return HttpResponse("File not valid")
	if csv_file.multiple_chunks():
		return HttpResponse("Uploaded file is big")
	# return HttpResponse(csv_file)
	
	file_data = csv_file.read().decode("UTF-8")
	lines = file_data.split("\n")
	c = len(lines)
	for i in range(0,c-1):
		fields = lines[i].split(",")
		data_dict = {}
		data_dict["Name"] = fields[0]
		data_dict["Addr"]=fields[1]
		data_dict["no_of_beds"]=fields[2]
		data_dict["no_of_doctors"]=fields[3]
		data_dict["no_of_staff"]=fields[4]
		data_dict["city"]=fields[5]
		data_dict["state"]=fields[6]
		data_dict["phone"]=fields[7]
		data_dict["email"]=fields[8]
		# return HttpResponse(fields[1])
		# return HttpResponse(data_dict)
		cform=hospitalForm(data_dict)
		if cform.is_valid():
			cform.save()
			
	return redirect("/hospital/viewHos/")

def download_hospital_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=Hospital.csv'
	writer = csv.writer(response)
	writer.writerow(['Name','Address','Number of Beds','Number of Doctors','Number of Staff','City','State','Phone','Email'])
	for data in hos.objects.all():
		writer.writerow([data.Name,data.Addr,data.no_of_beds,data.no_of_doctors,data.no_of_staff,data.city,data.state,data.phone,data.email])

	return response