from django.db import models
from register.models import user
# Create your models here.

class bmi(models.Model):
    userId = models.ForeignKey(user, to_field="username", on_delete=models.CASCADE)
    age = models.IntegerField(default=10)
    gender = models.CharField(max_length=20, default="male")
    user_weight = models.IntegerField(default=10)
    user_height = models.IntegerField(default=10)
    user_bmi = models.IntegerField(default=10)
    
    def save(self,*args, **kwargs):
        self.user_bmi=(self.user_height*self.user_weight)/10
        super(bmi, self).save(*args, **kwargs)

range = (
    (10,10),
    (20,20),
    (30,30),
    (40,40),
    (50,50),
    (60,60),
    (70,70),
    (80,80),
    (90,90),
    (100,100)
)

gender = (
    ("male","male"),
    ("female","female"),
)

ideal_height = (
    (70,70),
    (90,90),
    (110,110),
    (130,130),
    (150,150),
    (170,170),
    (190,190),
    (200,200),
    (220,220),
    (240,240),
)

class ideal_bmi(models.Model):
    age_range = models.IntegerField(choices=range)
    gender = models.CharField(max_length=20,choices=gender)
    ideal_weight = models.IntegerField(choices=range)
    ideal_height = models.IntegerField(choices=ideal_height)
    ideal_bmi = models.IntegerField()
    
    def save(self,*args, **kwargs):
        self.ideal_bmi=(self.ideal_height*self.ideal_weight)/10
        super(ideal_bmi, self).save(*args, **kwargs)