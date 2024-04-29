from django.db import models
from medhistory.models import medhistory
from register.models import *

# Create your models here. 
class prescription(models.Model):
    u_id = models.ForeignKey(user, to_field="username", on_delete=models.CASCADE)
    d_id = models.ForeignKey(doc, to_field="username", on_delete=models.CASCADE)
    medh_pres = models.ForeignKey(medhistory,on_delete=models.CASCADE,related_name='+')
    #med_name = models.ForeignKey(disease, on_delete=models.CASCADE)
    
    isavailable = models.BooleanField(default=False)
    
# patient Id, doctor id, medichistory me se prescription, 
# pharmacist me se medicine name, and 1 "is available" wala column, uska default false rahega.