from django.urls import path
from ..views import *

login_url = [
    path('login/', login_home, name='login-home'),
    path('loginuser/', login_request, name='user-login'),
    path('logindoctor/', login_doc_request, name='doc-login'),
    path('loginpharma/', login_pharma_request, name='pharma-login'),
    path('logout/', logout, name='logout'),
    path('loginadmin/',login_admin,name="login-admin"),
    
    #access the laptop camera
    path('video/', video, name='video'),

    path('download/<data>', base64_file, name='download'),
    path('downloadImage/', base64_file_image, name='download_image'),

    # profile
    path('userProfile/',userprofile, name="user-profile"),
    path('docProfile/',docprofile, name="doc-profile"),
    path('pharmaProfile/',pharmaprofile, name="pharma-profile"),
]

# redirect_authenticated_user=True, 