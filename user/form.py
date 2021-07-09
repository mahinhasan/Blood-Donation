from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.forms import Form
from .models import UserProfile



class SignUpForm(UserCreationForm):
#Add extra field in Form
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)
# Add 
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email",'username','password1','password2']

# Remove help text from signup form
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)   
        for f in ["first_name", "last_name", "email",'username','password1','password2']:
            self.fields[f].help_text=None



class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email",'username']
        def __init__(self, *args, **kwargs):
            super(SignUpForm,self).__init__(*args, **kwargs)   
            for f in [ "email",'username']:
                self.fields[f].help_text=None

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


    