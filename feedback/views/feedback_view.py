import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from register.models import *
from ..forms import *
from ..models import *

import logging
logger = logging.getLogger(__name__)



def viewFeedback(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    # context["disease"] = disease.objects.all()
    
    context["feedback"] = feedback.objects.all()
    return render(request, "feedback-view.html", context)

def deleteFeedback(request,id):
	context={}
	obj = get_object_or_404(feedback, id=id)
	if request.method == "GET":
		obj.delete()
        
		return redirect("/feedback/viewFeedback/")
	return render(request, "feedback-view.html", context)

def addFeedback(request):
    context = {}
    form = FeedbackForm(request.POST)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("Feedback was added")
        return redirect("/index")

    context['form'] = form
    return render(request, "feedback.html",context)

def user_addFeedback(request):
    context = {}
    form = FeedbackForm(request.POST)
    
    if form.is_valid():
        # return HttpResponse(form)
        form.save()
        logger.info("User Feedback was added")
        return redirect("/index")

    context['form'] = form
    return render(request, "user_feedback.html",context)


def download_feedback_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=feedback.csv'
	writer = csv.writer(response)
	writer.writerow(['Rating','Message',])
	for data in feedback.objects.all():
		writer.writerow([data.rating,data.message])

	return response