from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class medicine(models.Model):
    med_name = models.CharField(max_length=250)
    price = models.IntegerField(max_length=250)
    qty =models.IntegerField(max_length=250,null=True)
    image = models.ImageField(upload_to='medicine/medicine_img', null=True, blank=True)
    description = models.TextField(max_length=500, null=True)
    
