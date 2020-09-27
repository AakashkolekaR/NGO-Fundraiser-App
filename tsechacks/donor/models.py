from django.db import models
from django.utils.timezone import now
from employee.models import Event
# Create your models here.

class Donor(models.Model):
    dname=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    contact=models.CharField(max_length=40)
    pic_path=models.FileField(null=True,blank=True)

class Donations(models.Model):
    donor_id=models.ForeignKey(Donor,on_delete=models.CASCADE)
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE)
    collectedfunds=models.CharField(max_length=40)
    donationtype=models.CharField(max_length=40,default='money')
