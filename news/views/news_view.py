import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from register.models import user
from ..forms import *
from ..models import *


import logging
logger = logging.getLogger(__name__)

def viewNews(request):
    context = {}
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["news"] = news.objects.all()
    return render(request, "news-view.html", context)

def deleteNews(request,id):
	context={}
	obj = get_object_or_404(news, id=id)
	if request.method == "GET":
		obj.delete()
		logger.info("News Was Deleted")
		return redirect("/newss/viewNews/")
	return render(request, "news-view.html", context)

#def addNews(request):
#    context = {}
#    form = NewsForm(request.POST)
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
#    return render(request, "news/templates/news-add.html",context)


def addNews(request):

    form = NewsForm(request.POST,request.FILES)
    
    if form.is_valid():

        form.save()
		
        messages.success(request, "News Added Successfully")
        return redirect("/newss/viewNews/")
    
    return render(request, 'news-add.html')

def download_news_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=news.csv'
	writer = csv.writer(response)
	writer.writerow(['Title','Image',])
	for data in news.objects.all():
		writer.writerow([data.title,data.image])

	return response