from django.db import models
from register.models import *
from django.utils import timezone

# Create your models here.

class chat(models.Model):
    senderId = models.ForeignKey(user,to_field="username",on_delete=models.CASCADE, null=True, related_name = 'sender')
    receiverId = models.ForeignKey(user,to_field="username",on_delete=models.CASCADE, null=True, related_name = 'receiver')
    message = models.CharField(max_length=256)
    date = models.DateField(default=timezone.now(), null=True)