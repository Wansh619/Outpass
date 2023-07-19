from django.db import models
from datetime import datetime
# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=30)
    roll_no= models.CharField(max_length=8)
    reasons= models.CharField(max_length=1000)
    email=models.CharField(max_length=40)
    Date=models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.name

