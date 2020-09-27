from django.db import models
from django.utils.timezone import now

# Create your models here.


class Employee(models.Model):
    ename=models.CharField(max_length=40)
    eemail=models.CharField(max_length=40)
    eusername=models.CharField(max_length=40)
    epassword=models.CharField(max_length=40)
    econtact=models.CharField(max_length=40)
    epic_path=models.FileField(null=True,blank=True)

class marketeer(models.Model):
    mname=models.CharField(max_length=40)
    memail=models.CharField(max_length=40)
    musername=models.CharField(max_length=40)
    mpassword=models.CharField(max_length=40)
    mcontact=models.CharField(max_length=40)
    mpic_path=models.FileField(null=True,blank=True)

class Student(models.Model):
    sname=models.CharField(max_length=40)
    semail=models.CharField(max_length=40)
    scontact=models.CharField(max_length=40)
    sadd=models.CharField(max_length=200)
    sprog=models.CharField(max_length=200)
    scity=models.CharField(max_length=40)
    sgender=models.CharField(max_length=5)
    spic_path=models.FileField(null=True,blank=True)

class Event(models.Model):
    evname=models.CharField(max_length=40)
    evlocation=models.CharField(max_length=40,default='')
    evaddr=models.CharField(max_length=200)
    evdesc=models.CharField(max_length=200)
    evdur=models.CharField(max_length=40)
    evpic_path=models.FileField(null=True,blank=True)
    evdate=models.DateField(default=now,editable=False)
    evtype=models.CharField(max_length=40,default='education')
    ev_exfunds=models.CharField(max_length=40,default='10000')

class Comment(models.Model):
    comment=models.CharField(max_length=200)
    event_id=models.ForeignKey(Event,on_delete=models.CASCADE,default=None)
    username=models.CharField(max_length=40)
    sentiment=models.CharField(max_length=50,default='positive')
    cvdate=models.DateField(default=now,editable=False)

class Likes(models.Model):

    event_id=models.ForeignKey(Event,on_delete=models.CASCADE,default=None)
    username=models.CharField(max_length=40)
    
    cvdate=models.DateField(default=now,editable=False)
