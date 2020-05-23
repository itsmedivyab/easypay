
from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=150,blank=False)
    occup=models.CharField(max_length=150,blank=False)
    cardtype=models.CharField(max_length=150,blank=False)
    address=models.CharField(max_length=150,blank=False)
    phonenumber=models.CharField(max_length=10,blank=False)
    income=models.IntegerField(default=0,blank=False)
    bank=models.CharField(max_length=150,blank=False)
    email=models.EmailField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)
    cardno=models.CharField(max_length=16,unique=True,blank=False,default='')
    pan=models.CharField(max_length=100,blank=False,unique=False,default='')
    def __str__(self):
      return self.name
      
class historydata(models.Model):
     sender=models.CharField(max_length=150,blank=False)
     receiver=models.CharField(max_length=150,blank=False)
     amountsent=models.IntegerField(blank=False)
     date=models.CharField(max_length=2)    
     month=models.CharField(max_length=2)
     year=models.CharField(max_length=4)
     hrs=models.CharField(max_length=2,default='00')
     minutes=models.CharField(max_length=2,default='00')
     seconds=models.CharField(max_length=2,default='00')