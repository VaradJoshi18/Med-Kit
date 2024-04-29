from tkinter import CASCADE
from django.db import models
from register.models import doc,user

# Create your models here.
class medhistory(models.Model):
    #patient_id,patient_name(user)
    patientId = models.ForeignKey(user, to_field="username" , on_delete=models.CASCADE)
    doctorId = models.ForeignKey(doc, to_field="username", on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    problems = models.CharField(max_length=50)
    prescription = models.CharField(max_length=50)