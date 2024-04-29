from django.urls import path
from ..views import *

prescription_url = [
    path('prescriptionView/', viewPrescription, name="prescription-view"),
    path('prescriptionEdit/<id>', editPrescription, name="prescription-edit"),
    path('prescriptionDelete/<id>', deletePrescription, name="prescription-delete"),
    path('prescriptionAdd/', addPrescription, name="prescription-add"),
    path('downloadPrep',download_prescription_csv,name='download-prep'),

]