from django.contrib import admin
from .models import*
# Register your models here.


class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('incident','time')

admin.site.register(BloodRequest,BloodRequestAdmin)