from django.urls import path, include
from ..views import *
from django.conf import settings
from django.conf.urls.static import static

blog_url = [
    path('viewBlog/',viewBlog,name="blogs-view"),
    path('deleteBlog<id>/',deleteBlog,name="blog-delete"),
    # path('editBlog/<id>', editBlog, name="blog-edit"),
    path('addBlog',addBlog,name="blogs-add"),
    path('downloadBlog',download_blog_csv,name='download-blog'),

]