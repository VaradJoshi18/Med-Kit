from django.db import models

# Create your models here.
class user(models.Model):
        
    first_name = models.CharField(max_length=100)
    
    last_name = models.CharField(max_length=100)
    
    username = models.CharField(max_length=100, unique=True)
    
    email = models.EmailField()
    
    address = models.CharField(max_length=500)
    
    password1 = models.CharField(max_length=500)
    
    image = models.ImageField(upload_to='register/imgaes', null=True, blank=True)

    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    # pfp = models.ImageField(upload_to="avatars/")
    # REQUIRED_FIELDS = ('username','password1',)  
    # USERNAME_FIELD = 'username'
    
class doc(models.Model):
   
    name = models.CharField(max_length=100)
    
    age = models.IntegerField()
    experience = models.IntegerField()
    phone = models.BigIntegerField()
    
    hosName = models.CharField(max_length=100)
    hosLocation = models.CharField(max_length=500)
    
    username = models.CharField(max_length=100, unique=True)
    
    email = models.EmailField()
    
    degree = models.CharField(max_length=500)

    password = models.CharField(max_length=500)

    image = models.ImageField(upload_to='register/imgaes', null=True, blank=True)

    def __str__(self):
        return self.username

class pharma(models.Model):
    city = models.CharField(max_length=500)
    
    name = models.CharField(max_length=100)
    shopName = models.CharField(max_length=100)
    shopAddr = models.CharField(max_length=500)
    licenseNumber = models.IntegerField()
    
    username = models.CharField(max_length=100, unique=True)
    
    email = models.EmailField()
    nationwideDel = models.BooleanField()
    
    password = models.CharField(max_length=500)
    
    image = models.ImageField(upload_to='register/imgaes', null=True, blank=True)

    def __str__(self):
        return self.username
# def __str__(self):
# 		return self.title