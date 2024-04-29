from django.db import models
from tkinter import CASCADE

from traitlets import default
from register.models import doc,user
# Create your models here.



time = (
    ('10:00-11:00','10:00-11:00'),
    ('11:00-12:00','11:00-12:00'),
    ('12:00-1:00','12:00-1:00'),
    ('1:00-2:00','1:00-2:00'),
    ('2:00-3:00','2:00-3:00'),
    ('3:00-4:00','3:00-4:00'),
    ('4:00-5:00','4:00-5:00'),
    ('5:00-6:00','5:00-6:00'),
)

day = (
    ('MONDAY','MONDAY'),
    ('TUESDAY', 'TUESDAY'),
    ('WEDNESDAY','WEDNESDAY'),
    ('THURSDAY','THURSDAY'),
    ('FRIDAY','FRIDAY'),
    ('SATURDAY','SATURDAY'),
    ('SUNDAY','SUNDAY'),
)

status = (
    ('Pending' , 'Pending'),
    ('Accepted' , 'Accepted'),
    ('Rejected' , 'Rejected'),
)


class Appointment(models.Model):
    username = models.CharField(max_length=20)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    time = models.CharField(max_length=500,choices=time)
    day = models.CharField(max_length=500,choices=day)
    request = models.TextField(max_length=500)
    status = models.CharField(max_length=500,choices=status,default='Pending')
    doctorId = models.ForeignKey(doc, to_field="username", on_delete=models.CASCADE, null = True)

#class acceotappointment(models.Model):
#    doctorId = models.ForeignKey(doc, on_delete=models.CASCADE)
#    patientId = models.ForeignKey(user, on_delete=models.CASCADE)
#    status = models.CharField(max_length=500,choices=status,default=0)