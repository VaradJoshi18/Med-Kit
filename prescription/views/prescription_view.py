import csv
from ..forms import *
from ..models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


import logging
logger = logging.getLogger(__name__)


def viewPrescription(request):
    context = {}
    
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["prescription"] = prescription.objects.all()
    return render(request, "prescriptionview.html", context)

def addPrescription(request):
	context = {}
	form = RegisterPrescriptionForm(request.POST)

	if form.is_valid():
			
			form.save()
			logger.info("Prescription was added")
			return redirect("/prescription/prescriptionView/")

	context['form'] = form
	return render(request, "prescriptionAdd.html",context)

def deletePrescription(request,id):
	context={}
	obj = get_object_or_404(prescription, id=id)#
	if request.method == "GET":
		obj.delete()
		logger.info("Prescription was Deleted")
		return redirect("/prescription/prescriptionView/")
	return render(request, "prescriptionview.html", context)

def editPrescription(request,id):
    context = {}
    obj = get_object_or_404(prescription, id=id)
    form = RegisterPrescriptionForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
        return redirect("/prescription/prescriptionView/")
    
    context['form'] = form
    return render(request, "prescriptionAdd.html",context)

def download_prescription_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=prescription.csv'
	writer = csv.writer(response)
	writer.writerow(['User Id','Doctor Id','Med Prescription','Is Available'])
	for data in prescription.objects.all():
		writer.writerow([data.u_id,data.d_id,data.medh_pres,data.isavailable])

	return response