from django.db import models

# Create your models here.
import datetime
import os

# def filepath(request, filename):
#     old_filename = filename
#     timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
#     filename = "%s%s" % (timeNow, old_filename)
#     return os.path.join('uploads/', filename)

class news(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='news/news_img', null=True, blank=True)