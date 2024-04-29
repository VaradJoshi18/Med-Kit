from django.urls import path, include
from ..views import *
from django.conf import settings
from django.conf.urls.static import static

medicine_url = [
    path('viewMedicine/',viewMedicine,name="medicine-view"),
    path('deleteMedicine<id>/',deleteMedicine,name="medicine-delete"),
    path('editMedicine/<id>', editMedicine, name="medicine-edit"),
    path('addMedicine',addMedicine,name="medicine-add"),
    
    path('bulkupload1',bulk_upload1,name='bulkUpload1'),
    path('upload_csv1',upload_csv1,name='upload_csv1'),
    path('download',download_csv1,name='download1'),
]