from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from django.views import View
from register.models import user,doc,pharma

from ..forms import *
from ..models import *

def userside_viewToDoList(request):
    type = request.session.get('type')
    if type == 0:
        context = {}
        context['type'] = type
        username = request.session.get('username')
        context['username'] = username
        data = user.objects.filter(username=username)
        context['data'] = data
        context['user'] = user.objects.filter(username = username)
        context["todolist"] = ToDoList.objects.filter(username=username,type=0)
        return render(request, "user-ToDoList-view.html", context)
    elif type == 1:
        context = {}
        context['type'] = type
        username = request.session.get('username')
        context['username'] = username
        context['user'] = user.objects.filter(username = username)
        context["todolist"] = ToDoList.objects.filter(username=username,type=1)
        return render(request, "user-ToDoList-view.html", context)
    elif type == 2:
        context = {}
        context['type'] = type
        username = request.session.get('username')
        context['username'] = username
        context['user'] = user.objects.filter(username = username)
        context["todolist"] = ToDoList.objects.filter(username=username,type=2)
        return render(request, "user-ToDoList-view.html", context)

def userside_addToDoList(request):
    # type = request.session.get('type')
    context = {}
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username=username)
    context['data'] = data
    context['type'] = request.session.get('type')
        
    form = TodoListForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/todo/user_viewToDoList/")

    context['form'] = form
    return render(request, "user-todoList-add.html",context)

def userside_deleteToDoList(request,id):
    context={}
    obj = get_object_or_404(ToDoList, id=id)
    if request.method == "GET":
        obj.delete()
        return redirect("/todo/user_viewToDoList/")
    return render(request, "user-ToDoList-view.html", context)

def userside_editToDoList(request,id):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    context['type'] = request.session.get('type') 
    obj = get_object_or_404(ToDoList, id=id)
   
    form = TodoListForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/todo/user_viewToDoList/")
    
    context['form'] = form
    return render(request, "user-todoList-add.html",context)

# ==================================================================================
# TO-DO-ITEM
# ==================================================================================

def userside_viewToDoItem(request,title):
    context = {}
    # obj = get_object_or_404(ToDoItem, id=id)
    username = request.session.get('username')
    data = user.objects.filter(username=username)
    
    context['data'] = data
    context['todoList'] = title
    context['username'] = username
    
    # todolist_add = ToDoList.objects.filter(title=title)
    # # return HttpResponse(todolist_add)
    # context['todolist_add'] = todolist_add
    
    context["todoitem"] = ToDoItem.objects.filter(todo_list=title)
    return render(request, "user-todoItem-view.html", context)

def userside_addToDoItem(request,title):
    context = {}
    username = request.session.get('username')
    data = user.objects.filter(username=username)
    context['data'] = data
    context['username'] = username
    # ======================================================
    form = ToDoItemForm(request.POST)
    # context['todolist'] = title
    
    todolist_name = ToDoList.objects.filter(title=title)
    context['todolist_name'] = todolist_name
    # return HttpResponse(todolist_name)
    
    if form.is_valid():
        #return HttpResponse(form)
        form.save()
        return redirect("/todo/user_viewToDoList/")
    
    context['form'] = form
    return render(request, "user-todoItem-add.html",context)

def userside_deleteToDoItem(request,id):
	context={}
	obj = get_object_or_404(ToDoItem, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/todo/user_viewToDoList/")
	return render(request, "user-todoItem-view.html", context)

def userside_editToDoItem(request,id):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username=username)
    context['data'] = data
    
    obj = get_object_or_404(ToDoItem, id=id)
   
    form = ToDoItemForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/todo/viewToDoList/")
    
    context['form'] = form
    return render(request, "user-todoItem-add.html",context)