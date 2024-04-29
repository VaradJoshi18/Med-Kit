from django.urls import path, include
from ..views import *
from django.conf import settings
from django.conf.urls.static import static

news_url = [
    path('viewNews/',viewNews,name="news-view"),
    path('deleteNews<id>/',deleteNews,name="delete-news"),
#    path('editNews/<id>', editNews, name="edit-news"),
    path('addNews',addNews,name="news-add"),
    path('downloadNews',download_news_csv,name='download-news'),

]