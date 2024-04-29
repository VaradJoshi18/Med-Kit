from django.urls import path
from ..views import *

reg_url_list = [
    # path('home/', reg_home, name='users-home'),
    path('main/', MainView.as_view(), name='main-view'), 
    path('register/', RegisterView.as_view(), name='users-register'),
    path('registerDoctor/', RegisterDocView.as_view(), name='doctor-register'),
    path('registerPharma/', RegisterPharmaView.as_view(), name='pharma-register'),
    path('viewDoctors/', view_doctors, name="user-side-doctor-view"),
    # path('log/', CustomLoginView.as_view(template_name='login.html', 
    # authentication_form=LoginForm), name='log')     #redirect_authenticated_user=True,
]