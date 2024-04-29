from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from register.models import user
from ..forms import *
from ..models import *

def viewToDoList(request):
    context = {}
    
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    context["todolist"] = ToDoList.objects.filter(username=username)
    return render(request, "ToDoList-view.html", context)

def addToDoList(request):
	context = {}
	form = TodoListForm(request.POST)

	if form.is_valid():
			form.save()
			return redirect("/todo/viewToDoList/")

	context['form'] = form
	return render(request, "ToDoListAdd.html",context)

def deleteToDoList(request,id):
	context={}
	obj = get_object_or_404(ToDoList, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/todo/viewToDoList/")
	return render(request, "ToDoList-view.html", context)

def editToDoList(request,id):
    context = {}    
    obj = get_object_or_404(ToDoList, id=id)
   
    form = TodoListForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/todo/viewToDoList/")
    
    context['form'] = form
    return render(request, "ToDoListAdd.html",context)

# ==================================================================================
# TO-DO-ITEM
# ==================================================================================

def viewToDoItem(request,title):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    context["todoitem"] = ToDoItem.objects.filter(todo_list=title)
    return render(request, "ToDoItem-view.html", context)

def addToDoItem(request):
	context = {}
	form = ToDoItemForm(request.POST)
	
	if form.is_valid():
			form.save()
			return redirect("/todo/viewToDoList/")

	context['form'] = form
	return render(request, "ToDoItemAdd.html",context)

def deleteToDoItem(request,id):
	context={}
	obj = get_object_or_404(ToDoItem, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/todo/viewToDoList/")
	return render(request, "ToDoItem-view.html", context)

def editToDoItem(request,id):
    context = {}    
    obj = get_object_or_404(ToDoItem, id=id)
   
    form = ToDoItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/todo/viewToDoList/")
    
    context['form'] = form
    return render(request, "ToDoItemAdd.html",context)