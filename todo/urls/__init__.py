from .todo_url import to_do_url, to_do_item_url,userside_todolist_url, userside_todoitem_url

urlpatterns = to_do_url + to_do_item_url + userside_todolist_url + userside_todoitem_url
