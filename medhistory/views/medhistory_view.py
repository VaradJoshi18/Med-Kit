import csv
from ..forms import *
from ..models import *
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404


import logging
logger = logging.getLogger(__name__)


def viewMedhistory(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["medhistory"] = medhistory.objects.all()
    return render(request, "medhistoryview.html", context)

def addMedhistory(request):
	context = {}
	form = RegisterMedhistoryForm(request.POST)

	if form.is_valid():
			
			form.save()
			logger.info("Medical History was added")
			return redirect("/medhistory/medhistoryView/")

	context['form'] = form
	return render(request, "medhistoryAdd.html",context)

def deleteMedhistory(request,id):
	context={}
	obj = get_object_or_404(medhistory, id=id)#
	if request.method == "GET":
		obj.delete()
		logger.info("Medical History was Deleted")
		return redirect("/medhistory/medhistoryView/")
	return render(request, "medhistoryview.html", context)

def editMedhistory(request,id):
    context = {}
    obj = get_object_or_404(medhistory, id=id)
    form = RegisterMedhistoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
        return redirect("/medhistory/medhistoryView/")
    
    context['form'] = form
    return render(request, "MedhistoryAdd.html",context)


def download_medhis_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=medhistory.csv'
	writer = csv.writer(response)
	writer.writerow(['Patient Id','Doctor Id','Date','Problems','Prescription'])
	for data in medhistory.objects.all():
		writer.writerow([data.patientId,data.doctorId,data.date,data.problems,data.prescription])

	return response

def docsideMedHistory_view(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    
    doctor = doc.objects.filter(username=username)
    doc_id = doctor[0]
    context['doc'] = doctor
    data = medhistory.objects.filter(doctorId = doc_id)
    context['medhis'] = data

    return render(request,"docside-medhistory-view.html",context)