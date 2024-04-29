from django.urls import path
from ..views import *

to_do_url = [
    # path('home/', todo_home, name='users-home'),
    path('viewToDoList/', viewToDoList, name='todolist-view'),
    path('addToDoList/', addToDoList, name='todolist-add'),
    path('deleteToDoList/<id>', deleteToDoList, name='todolist-delete'),
    path('editToDoList/<id>', editToDoList, name='todolist-edit'),
]

to_do_item_url = [
    # path('home/', todo_home, name='users-home'),
    path('viewToDoItem/<title> ', viewToDoItem, name='todoItem-view'),
    path('addToDoItem/', addToDoItem, name='todoItem-add'),
    path('deleteToDoItem/<id>', deleteToDoItem, name='todoItem-delete'),
    path('editToDoItem/<id>', editToDoItem, name='todoItem-edit'),
]

userside_todolist_url = [
    path('user_viewToDoList/', userside_viewToDoList, name='user-todoList-view'),
    path('user_addToDoList/', userside_addToDoList, name='user-todoList-add'),
    path('user_editToDoList/<int:id>', userside_editToDoList, name='user-todoList-edit'),
    path('user_deleteToDoList/<int:id>', userside_deleteToDoList, name='user-todoList-delete'),
]

userside_todoitem_url = [
    path('user_viewToDoItem/<title>', userside_viewToDoItem, name='user-todoItem-view'),
    path('user_addToDoItem/<title>', userside_addToDoItem, name='user-todoItem-add'),
    path('user_editToDoItem/<int:id>', userside_editToDoItem, name='user-todoItem-edit'),
    path('user_deleteToDoItem/<int:id>', userside_deleteToDoItem, name='user-todoItem-delete'),
]