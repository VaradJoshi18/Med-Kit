from django.db import models

from disease.models import disease

# Create your models here.
class treatment(models.Model):
    idd = models.ForeignKey(disease, to_field="name", on_delete=models.CASCADE)# Name rather than id?
    remedies_1 = models.CharField(max_length=50)
    remedies_2 = models.CharField(max_length=50)
    remedies_3 = models.CharField(max_length=50)