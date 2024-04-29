from django.urls import path
from ..views import *

contacturl = [
    path('viewContact/', viewContact, name="view-contact"),
    path('deleteContact<id>/', deleteContact, name="delete-contact"),
    path('addContact/', addContact, name="add-contact"),
    path('editContact<id>/', editContact, name="edit-contact"),
    path('downloadContact',download_contact_csv,name='download-contact'),

]