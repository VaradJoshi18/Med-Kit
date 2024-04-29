from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from ..models import chat
from ..forms import chatForm
from register.models import user
import csv
from django.db.models import Q

# ADMIN SIDE

def chatView(request):
    context = {}
    
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username="Admin")
    context['data'] = data
    
    data = chat.objects.filter(Q(senderId=username) | Q(receiverId = username))
    context['chat'] = data
    
    return render(request,"chatView.html",context)

def chatAdd(request):
    context = {}
    form = chatForm(request.POST)
	# form.cleaned_data['datetime'] = timezone.now()
    if form.is_valid():
        form.save()
		# logger.info("BMI was added")
        return redirect("/chat/viewChat/")

    context['form'] = form
    return render(request, "chatAdd.html",context)

def userchatDelete(request,id):
	context={}
	obj = get_object_or_404(chat, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/chat/chat_view/")
	return render(request, "chatView.html", context)

def chatDelete(request,id):
	context={}
	obj = get_object_or_404(chat, id=id)
	if request.method == "GET":
		obj.delete()
		return redirect("/chat/viewChat/")
	return render(request, "chatView.html", context)

def chatEdit(request,id):
    context={}   
    obj = get_object_or_404(chat, id=id)
   
    form = chatForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
		
        return redirect("/chat/viewChat/")
    
    context['form'] = form
    return render(request, "chatAdd.html",context)

# USER SIDE

def user_chat(request):
    context = {}
    
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username=username)
    context['data'] = data
    
    user_chats = chat.objects.order_by().values('senderId').distinct()
    # return HttpResponse(user_chats)
    context['user_chats'] = user_chats
    
    chat_data = chat.objects.filter(Q(senderId=username) | Q(receiverId=username))
    context['chat'] = chat_data
    
    return render(request, "user-chatView.html", context)

def user_chat_add(request):
    context = {}
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username=username)
    context['data'] = data
    
    return render(request,"user-chatAdd.html",context)

def single_chat_view(request,user_chat):
    context={}
    
    # default block 
    username = request.session.get('username')
    context['username'] = username
    data = user.objects.filter(username=username)
    context['data'] = data
    user_chats = chat.objects.order_by().values('senderId').distinct()
    # return HttpResponse(user_chats)
    context['user_chats'] = user_chats
    # end default block
    
    chat_data = chat.objects.filter(Q(senderId=user_chat) | Q(receiverId=user_chat)).order_by('date')
    context['chat'] = chat_data
    
    
    context['user_chat'] = user_chat
    return render(request,"single-chat-view.html",context)