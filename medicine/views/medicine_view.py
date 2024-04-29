import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from matplotlib.style import context
from ..forms import *
from ..models import *
from register.models import *


import logging
logger = logging.getLogger(__name__)

def viewMedicine(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["medicine"] = medicine.objects.all()
    return render(request, "medicine-view.html", context)

def deleteMedicine(request,id):
	context={}
	obj = get_object_or_404(medicine, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/medicine/viewMedicine/")
	return render(request, "medicine-view.html", context)

#def addBlog(request):
#    context = {}
#    form = BlogForm(request.POST)
#    
#    if form.is_valid():
#        # return HttpResponse(form)
#        if len(request.FILES) != 0:
#            form.image = request.FILES['image']
#        
#        form.save()
#        messages.success(request, "Blog added successfully")
#        return redirect("/index")
#
#    context['form'] = form
#    return render(request, "news/templates/blog-add.html",context)




def addMedicine(request):
	context={}
	
	form = RegisterMedicineForm(request.POST,request.FILES)
	# return HttpResponse(form)
	if form.is_valid():
		form.save()
		# return HttpResponse(form)
		logger.info("Medicine was added")
		messages.success(request, "Medicine Added Successfully")
		return redirect("/medicine/viewMedicine/")
	else:
		print("Hello")

	context['form_user'] = form
	return render(request, 'medicine-add.html',context)

def editMedicine(request,id):
    context = {}
    obj = get_object_or_404(medicine, id=id)
    form = RegisterMedicineForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() #
		
        return redirect("/medicine/MedicineView/")
    
    context['form'] = form
    return render(request, "medicineAdd.html",context)

def bulk_upload1(request):
	return render(request,"bulkUpload1.html")

def upload_csv1(request):
	if request.method == 'GET':
		return render(request, "bulkUpload1.html")
		
		# return HttpResponse("Not Valid method")
		
	csv_file=request.FILES['csv_file1']
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
		data_dict["med_name"] = fields[0]
		data_dict["price"]=fields[1]
		data_dict["qty"]=fields[2]
		data_dict["image"]=fields[3]
		data_dict["description"]=fields[4]
		# return HttpResponse(fields[1])
		cform=RegisterMedicineForm(data_dict)
		# return HttpResponse(data_dict)
		if cform.is_valid():
			cform.save()
			
	return redirect("/medicine/viewMedicine/")

def download_csv1(request):
	response=HttpResponse()
	response['content-Disposition'] = 'attachment; filename=medicine.csv'
	writer = csv.writer(response)
	writer.writerow(['Medicine Name','Price','Quantity','Image','Description'])
	for data in medicine.objects.all():
		writer.writerow([data.med_name,data.price,data.qty,data.image,data.description])

	return response