from django.db import models
from django.contrib.auth.models import User
from . choice import groups,districts,divisions
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
#from phonenumber_field.modelfields import PhoneNumberField





class BloodDoner(models.Model):
    name = models.CharField(max_length=50,blank=True)
    group = models.CharField(max_length=50 , choices=groups,blank=True,null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField( max_length=50)
    district = models.CharField(max_length=50,choices = districts,blank=True,null=True)
    division = models.CharField(max_length=50,choices = divisions)
    country = models.CharField(max_length=50)
    is_given = models.BooleanField(null=True)
    given_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    
    #link = models.URLField(max_length=200)

    def __str__(self):
        return ("Name: "+self.name+" ("+self.group+")")

class Artical(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank = True,null=True)
    image = models.ImageField( upload_to="articalImage/",blank=True,null=True, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return (self.title)

class CreatePost(models.Model):
    
    title = models.CharField( max_length=250)
    group = models.CharField(max_length=50 , choices=groups)
    phone = models.CharField( max_length=50) 
    district = models.CharField(max_length=50,choices = districts)
    division = models.CharField(max_length=50,choices = divisions)
    country = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now=True)
    email = models.EmailField(max_length=100)
    body = models.TextField(blank = True,null=True)

    


    def __str__(self):
        return (self.title+"  ("+self.group+")")


class Hospital(models.Model):
    name = models.CharField(max_length=240)
    district = models.CharField(max_length=100, choices=districts)
    area = models.CharField(max_length=250,null=True,blank=True)
    hospital_number = models.CharField(max_length=20)
    ambulance_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Ambulance(models.Model):
    driver_name = models.CharField(max_length=240)
    district = models.CharField(max_length=100, choices=districts)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True,blank=True)
    ambulance_number = models.CharField(max_length=20)

    def __str__(self):
        return self.driver_name


