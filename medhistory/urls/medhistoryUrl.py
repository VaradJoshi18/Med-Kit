from django.urls import path
from ..views import *

medhistory_url = [
    path('medhistoryView/', viewMedhistory, name="medhistory-view"),
    path('medhistoryEdit/<id>', editMedhistory, name="medhistory-edit"),#id
    path('medhistoryDelete/<id>', deleteMedhistory, name="medhistory-delete"),#
    path('medhistoryAdd/', addMedhistory, name="medhistory-add"),
    path('downloadMedhis',download_medhis_csv,name='download-medhis'),
    path('docside-medhistory-view', docsideMedHistory_view, name='docside-medhistory-view')
]