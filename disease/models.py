from django.db import models

# Create your models here.
class disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    symptom_1 = models.CharField(max_length=50)
    symptom_2 = models.CharField(max_length=50)
    symptom_3 = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name