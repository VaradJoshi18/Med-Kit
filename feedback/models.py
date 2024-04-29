from django.db import models

# Create your models here.

class feedback(models.Model):
    class Rating_options(models.IntegerChoices):
        very_good = 5
        good = 4
        average = 3
        not_good = 2
        bad = 1
    rating = models.IntegerField(choices=Rating_options.choices)
    message = models.TextField(max_length=500)