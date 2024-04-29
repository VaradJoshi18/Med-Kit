from django.urls import path
from ..views import *

chat_url = [
    path("viewChat/",chatView,name="view-chat"),
    path("addChat/",chatAdd,name="add-chat"),
    path("deleteChat/<int:id>",chatDelete,name="delete-chat"),
    path("deleteuserChat/<int:id>",userchatDelete,name="delete-user-chat"),
    path("editChat/<int:id>",chatEdit,name="edit-chat"),
    # user side
    path("chat_view/",user_chat,name="user-chat-view"),
    path("chat_add/",user_chat_add,name="user-chhat-add"),
    path("single_chat_view/<user_chat>",single_chat_view,name="single-chat-view"),
]