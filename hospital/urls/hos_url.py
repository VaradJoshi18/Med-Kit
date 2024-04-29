from django.urls import path
from ..views import *

hosurl = [
    path('viewHos/', viewhos, name="view-hos"),
    path('addHos/', addhos, name="add-hos"),
    path('deleteHos<id>/', deletehos, name="delete-hos"),
    path('editHos<id>/', edithos, name="edit-hos"),
    path('downloadHos',download_hospital_csv,name='download-hos'),
    path('bulkupload2',bulk_upload2,name='bulkUpload2'),
    path('upload_csv2',upload_csv2,name='upload_csv2'),

]