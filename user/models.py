from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.signals import user_logged_out
from django.db.models.base import Model
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'Logged out.')




class UserProfile(Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    time = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.user.username 
