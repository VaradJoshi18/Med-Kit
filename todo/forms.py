from dataclasses import field
from django import forms
from .models import *
 
class TodoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields="__all__"
        
class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields=['title','description','todo_list']