from django.urls import path
from ..views import *

treatment_url = [
    path('treatView/', viewTreatment, name="treatment-view"),
    path('treatEdit/<id>', editTreatment, name="treatment-edit"),#id
    path('treatDelete/<id>', deleteTreatment, name="treatment-delete"),#
    path('treatAdd/', addTreatment, name="treatment-add"),
    path('downloadTreat',download_treatment_csv,name='download-treat'),

]