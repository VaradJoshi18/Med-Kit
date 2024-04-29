import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from register.models import user

from ..models import *
from ..forms import *

import logging
logger = logging.getLogger(__name__)

def viewContact(request):
    context = {}
    
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["contact"] = contact.objects.all()
    return render(request, "contact-view.html", context)

def deleteContact(request,id):
	context={}
	obj = get_object_or_404(contact, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/contact/viewContact/")
	return render(request, "contact-view.html", context)

def addContact(request):
    context = {}
    form = ContactForm(request.POST)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("Contact Added")
        return redirect("/index")

    context['form'] = form
    return render(request, "contact.html",context)

def user_addContact(request):
    context = {}
    form = ContactForm(request.POST)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("User Contact Added")

        return redirect("/index/")

    context['form'] = form
    return render(request, "user_contact.html",context)

def editContact(request,id):
    context = {}
    obj = get_object_or_404(contact, id=id)
    form = ContactForm(request.POST or None, instance=obj)

    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("Contact Edited")

        return redirect("/contact/viewContact/")

    context['form'] = form
    return render(request, "editContact.html",context)

def download_contact_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=contact.csv'
	writer = csv.writer(response)
    #name,email,subject,message,solved
	writer.writerow(['Name','Email','Subject','Message','Solved'])
	for data in contact.objects.all():
		writer.writerow([data.name,data.email,data.subject,data.message,data.solved])

	return response