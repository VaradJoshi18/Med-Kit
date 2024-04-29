from django.urls import path
from ..views import *

disease_url = [
    path('diseaseView/', viewDisease, name="disease-view"),
    path('diseaseEdit/<id>', editDisease, name="disease-edit"),#id
    path('diseaseDelete/<id>', deleteDisease, name="disease-delete"),#
    path('diseaseAdd/', addDisease, name="disease-add"),

    path('bulkupload',bulk_upload,name="bulkUpload"),
    path('upload_csv',upload_csv,name='upload_csv'),
    path('downloadDisease',download_disease_csv,name='download-disease')
]