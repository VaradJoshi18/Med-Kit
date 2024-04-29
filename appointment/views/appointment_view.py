import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from ..models import *
from ..forms import *

import logging
logger = logging.getLogger(__name__)
#logger = logging.getLogger('django')

def viewAppointment(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["appointment"] = Appointment.objects.all()
    logger.info("Appointment has been viewed")
    return render(request, "appointment-view.html", context)

def deleteAppointment(request,id):
	context={}
	obj = get_object_or_404(Appointment, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/appointment/viewuserappointment/")
	return render(request, "user-side-appointment.html", context)

def addAppointment_UserProfile(request):
    context = {}
    form = UserAppointmentForm(request.POST)
    username = request.session.get('username')
    context['user'] = user.objects.filter(username = username)
    context['user_username'] = username
    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        logger.info("User appointment has been added")
        return redirect("/appointment/viewuserappointment/")

    context['form_user'] = form
    return render(request, "user-side-appointment-add.html", context)

# index page view:
def addAppointmentUser(request):
    context = {}
    form = UserAppointmentForm(request.POST)
    username = request.session.get('username')
    

    context['user_username'] = username
    if form.is_valid():
        #return HttpResponse(form)
        app = form.save(commit=False)
        time = app.time
        day = app.day
        request1 = app.request
        email = app.email
        fname = app.fname
        lname = app.lname
        doctorId = request.POST['doctorId']

        #Email
        recipient_email = request.POST.get("email")
        subject = "Appointment Has been Recorded"
        message = "Hello, \n"+username+" we have recorded your Appointment \n\nTime: "+time+"\nDay "+day+"\nFor Request: "+request1+" \n\n We will let you know on("+email+") once it has been approved \n\n Thank you\n"+fname +" "+ lname
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient_email]
        # return HttpResponse(message)
        send_mail( subject, message, email_from, recipient_list, fail_silently=False )
        #########
        logger.info("User appointment has been added")
        app.save()
        return redirect("/index/")

    context['form_user'] = form
    return render(request, "index.html", context)


def viewAppointment_UserSide(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    context['user'] = user.objects.filter(username = username)
    context['Appdata'] = Appointment.objects.all()
    
    data = user.objects.filter(username=username)
    context['data'] = data
    
    logger.info("Appointment has been viewed")
    return render(request, "user-side-appointment.html", context)

# profile page view:
def addAppointment_UserSide(request):
    context = {}
    form = UserAppointmentForm(request.POST)
    
    if form.is_valid():
        form.save()
        
        
        logger.info("User appointment has been added")
        return redirect("/doctors/")

    context['form_user'] = form
    return render(request, "doctors.html", context)

#def acceptappointment(request):
#    context = {}
#    form = AcceptAppointmentForm(request.POST)
#    
#    if form.is_valid():
#        # return HttpResponse(form)
#        form.save()
#        return redirect("/appointment/viewappointment")
#
#    context['form'] = form
#    return render(request, "appointment-accept.html",context)

# fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=200)
#     time = models.CharField(max_length=500,choices=time)
#     day = models.CharField(max_length=500,choices=day)
#     request = models.TextField(max_length=500)
#     status = models.CharField(max_length=500,choices=status,default='Pending')
#     doctorId = models.IntegerField(null=True,default=0)

def download_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=appointment.csv'
	writer = csv.writer(response)
	writer.writerow(['First Name','Last Name','Email','Time','Day','Request','Status','Doctor Id'])
	for data in Appointment.objects.all():
		writer.writerow([data.fname,data.lname,data.email,data.time,data.day,data.request,data.status,data.doctorId])

	return response

def docside_appointemnt(request):
    context = {}
    
    username = request.session.get('username')
    doctor = doc.objects.filter(username=username)
    # docId = doctor[0]
    data = Appointment.objects.filter(status = "Pending")
    
    context['data'] = data
    context['username'] = username
    context['user'] = doctor
    return render(request,"docside-appointment.html",context)

def fix_appointment(request,id):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    
    doctor = doc.objects.filter(username=username)
    docId = doctor[0]
    context['docId'] = docId
    context['user'] = doctor
    
    obj = get_object_or_404(Appointment, id=id)
    
    # context['id']=obj['id']
    # context['fname']=obj[1]
    # context['lname']=obj[2]
    # context['email']=obj[3]
    # context['time']=obj[4]
    # context['day']=obj[5]
    # context['request']=obj[6]
    # context['status']="Approved"
    # context['doctorId']=docId
    # context['username']=obj[9]
    
    form = AcceptAppointmentForm(request.POST or None, instance=obj)
    # return HttpResponse(form)
    if form.is_valid():
        form.save()
        return redirect("/appointment/docside-viewappointment/")
    
    context['form'] = form
    
    return render(request,'fix-appointment.html',context)

def view_own_appointment(request):
    context = {}
    username = request.session.get('username')
    doctor = doc.objects.filter(username=username)
    docId = doctor[0]
    
    context['username'] = username
    context['user'] = doctor

    app = Appointment.objects.filter(doctorId = docId, status="Accepted")
    context['data'] = app
    return render(request,"doc-own-appointment.html",context)