from django.urls import path
from ..views import *

a_url = [
    path('home/', index, name="home"),
]