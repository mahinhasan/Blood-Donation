from django.db import models
from django.db.models.base import Model
from .choice import *
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class BloodRequest(models.Model):
    incident = models.CharField(max_length=254)
    blood_group = models.CharField(max_length=50 , choices=groups,default='A+')
    contact = models.CharField( max_length=50,null=True,blank=True) 
    district = models.CharField(max_length=50,choices = districts,default='Dhaka')
    division = models.CharField(max_length=50,choices = divisions,default='Dhaka')
    blood_need = models.DateTimeField(null=True,auto_now_add=False,default=datetime.now, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    content = models.TextField(blank = True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return self.incident