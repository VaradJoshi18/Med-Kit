from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import timeline, timeline_doc, timeline_pharma
from ..forms import timelineForm, timeline_pharmaForm, timeline_docForm,user_timeline_edit_Form
from django.utils import timezone
from register.models import user,doc,pharma

#==================ADMIN==========================================
def viewAdminTime(request):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    
    context['username'] = request.session.get('username')
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context = {"user":timeline.objects.all(), "doc":timeline_doc.objects.all(), "pharma": timeline_pharma.objects.all()}
    return render(request, "timeline-view.html", context)

#==================USER===========================================
def viewTime(request):
    context = {}
    context['username'] = request.session.get('username')
    # context['image'] = request.session.get('image')
    username = request.session.get('username')
    data = user.objects.filter(username=username)
    context['data'] = data
    
    context['user'] = user.objects.filter(username = username)
    # return HttpResponse(username)
    user_filter = user.objects.filter(username = username)
    uid = user_filter[0]
    # uid = user_filter.first()
    # uid = 1
    context["timeline"] = timeline.objects.filter(userId=uid)
    return render(request, "userside-view-time.html", context)

def addTime(request):
    context = {}
    
    username = request.session.get('username')
    context['username'] = username
    context['user'] = user.objects.filter(username=username)
    
    form = timelineForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline/")
    context['form'] = form
    return render(request, "timelineAdd.html",context)

def deleteTime(request,id):
	context={}
	obj = get_object_or_404(timeline, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/timeline/viewTimeline/")
	return render(request, "userside-view-time.html", context)

def editTime(request,id):
    context = {}    
    obj = get_object_or_404(timeline, id=id)

    username = request.session.get('username')
    context['username'] = username
    context['user'] = user.objects.filter(username=username)
    
    form = user_timeline_edit_Form(request.POST or None, instance=obj)
    # return HttpResponse(form)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline/")
    
    context['form'] = form
    return render(request, "edit-time.html",context)

#============DOCTOR======================================================

def viewdocTime(request):
    context = {}
    context['username'] = request.session.get('username')
    username = request.session.get('username')
    doc_filter = doc.objects.filter(username = username)
    docid = doc_filter[0]
    # obj = get_object_or_404(ToDoItem, id=id)
    context["timeline"] = timeline_doc.objects.filter(docId=docid)
    return render(request, "docside-view-time.html", context)

def adddocTime(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    context['doc'] = doc.objects.filter(username=username)
 
    form = timeline_docForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline-doc/")
    
    context['form'] = form
    return render(request, "doctimelineAdd.html",context)

def deletedocTime(request,id):
	context={}
	obj = get_object_or_404(timeline_doc, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/timeline/viewTimeline-doc/")
	return render(request, "docside-view-time.html", context)

def editdocTime(request,id):
    context = {}    
    obj = get_object_or_404(timeline_doc, id=id)
    
    username = request.session.get('username')
    context['username'] = username
    context['doc'] = doc.objects.filter(username=username)
    
    form = timeline_docForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline-doc/")
    
    context['form'] = form
    return render(request, "doctimelineAdd.html",context)

#============PHARMACIST======================================================

def viewpharmaTime(request):
    context = {}
    context['username'] = request.session.get('username')
    username = request.session.get('username')
    pharma_filter = pharma.objects.filter(username = username)
    pharmaid = pharma_filter[0]
    # obj = get_object_or_404(ToDoItem, id=id)
    context["timeline"] = timeline_pharma.objects.filter(pharmaId=pharmaid)
    return render(request, "pharmaside-view-time.html", context)

def addpharmaTime(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    context['pharma'] = pharma.objects.filter(username=username)
 
    form = timeline_pharmaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline-pharma/")
    
    context['form'] = form
    return render(request, "pharmatimelineAdd.html",context)

def deletepharmaTime(request,id):
	context={}
	obj = get_object_or_404(timeline_pharma, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/timeline/viewTimeline-pharma/")
	return render(request, "pharmaside-view-time.html", context)

def editpharmaTime(request,id):
    context = {}    
    obj = get_object_or_404(timeline_pharma, id=id)
    
    username = request.session.get('username')
    context['username'] = username
    context['pharma'] = pharma.objects.filter(username=username)
    
    form = timeline_pharmaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/timeline/viewTimeline-pharma/")
    
    context['form'] = form
    return render(request, "pharmatimelineAdd.html",context)