from django.db import models
from datetime import datetime
# Create your models here.
class Students(models.Model):
    roll_no= models.CharField(max_length=8,primary_key=True)
    name= models.CharField(max_length=30)
    reasons= models.CharField(max_length=1000)
    email=models.CharField(max_length=40)
    From=models.DateTimeField(default=datetime.now,blank=True)
    To=models.DateTimeField(default=None,blank=True)
    
    def __str__(self):
        return self.roll_no

