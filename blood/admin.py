from django.contrib import admin
from django.db import models

# Register your models here.
from .models import BloodDoner,Artical,CreatePost,Hospital,Ambulance

class Post(admin.ModelAdmin):
    list_display=('title','group','district')

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name','district','ambulance_number')

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('driver_name','district','ambulance_number')
admin.site.register(BloodDoner)
admin.site.register(CreatePost,Post)
admin.site.register(Artical)
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Ambulance,AmbulanceAdmin)