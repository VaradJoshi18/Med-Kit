from django.urls import path
from ..views import *

m_url = [
    path('viewDoc/', viewDoc, name="view-doc"),
    path('editDoc/<id>', editDoc, name="edit-doc"),
    path('deleteDoc/<id>', deleteDoc, name="delete-doc"),
    path('addDoc/', addDoc, name="add-doc"),

    path('viewPharma/', viewPharma, name="view-pharma"),
    path('editPharma/<id>', editPharma, name="edit-pharma"),
    path('deletePharma/<username>', deletePharma, name="delete-pharma"),
    path('addPharma/', addPharma, name="add-pharma"),

    path('viewUser/', viewUser, name="view-user"),
    path('editUser/<id>', editUser, name="edit-user"),
    path('deleteUser/<username>', deleteUser, name="delete-user"),
    path('addUser/', addUser, name="add-user"),

    path('downloadDoc',download_doc_csv,name='download-doc'),
    path('downloadUser',download_user_csv,name='download-user'),
    path('downloadPharma',download_pharma_csv,name='download-pharma'),
] 