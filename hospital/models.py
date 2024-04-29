from django.db import models
from register.models import doc
# Create your models here
class hos(models.Model):
   
    Name = models.CharField(max_length=200)
    Addr = models.CharField(max_length=200)
        
    no_of_beds = models.IntegerField()
    no_of_doctors = models.IntegerField()
    no_of_staff = models.BigIntegerField()
    
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    phone = models.BigIntegerField()
    email = models.EmailField()