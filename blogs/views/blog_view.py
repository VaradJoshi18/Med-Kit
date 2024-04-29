import csv
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from ..forms import *
from ..models import *
from register.models import user
from django.contrib.auth.hashers import make_password


import logging
logger = logging.getLogger(__name__)

def viewBlog(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["blogs"] = blog.objects.all()
    return render(request, "blogs-view.html", context)

def deleteBlog(request,id):
	context={}
	obj = get_object_or_404(blog, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/blogss/viewBlog/")
	return render(request, "blogs-view.html", context)

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

# def editBlog(request,id):
# 	context = {}
# 	obj = get_object_or_404(blog, id=id)
# 	form = BlogForm(request.POST or None, instance=obj)
# 	if form.is_valid():
# 		sign_up = form.save(commit=False)
# 		sign_up.save()
# 		return redirect("/blogss/viewBlog/")

# 	context['form'] = form
# 	return render(request, "blogs-add.html",context)

def addBlog(request):

    form = BlogForm(request.POST,request.FILES)
          
    if form.is_valid():

        form.save()
        logger.info("Blog was added")

        messages.success(request, "Blog Added Successfully")
        return redirect("/blogss/viewBlog/")
    
    return render(request, 'blogs-add.html')

def download_blog_csv(request):
	response=HttpResponse('txt/csv')
	response['content-Disposition'] = 'attachment; filename=blog.csv'
	writer = csv.writer(response)
	writer.writerow(['Title','Image','Details',])
	for data in blog.objects.all():
		writer.writerow([data.title,data.image,data.details])

	return response