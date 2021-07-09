from django import forms
from django.db.models import fields
from django.forms import widgets
from br.models import BloodRequest
from .models import Ambulance, BloodDoner, CreatePost, Hospital
from br.date_time import MinimalSplitDateTimeMultiWidget

"""
name = mode
group = mod
age = model
pic = model
phone = mod
district = 
division = 
country = m
is_given = 
given_date 
email = mod
"""
class CreateForm(forms.ModelForm):
    blood_need = forms.DateTimeField(widget=MinimalSplitDateTimeMultiWidget())
    class Meta:
        model = BloodRequest
        fields = ('incident','blood_group','contact','district','division','email','blood_need','content')

        widgets = {
            'content': forms.Textarea(attrs={
               
                'cols': 200, 'rows': 2,
                'placeholder':'Full breif why you need blood?'
                
                }),

                
        }

class DonerForm(forms.ModelForm):
    class Meta:
        model = BloodDoner
        fields = '__all__' 

      
class SearchForm(forms.ModelForm):
    class Meta:
        model = BloodDoner
        fields = ('group','district')

class HospitalAddForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('name','district')
        name = forms.CharField( label="Enter Title:", widget=forms.TextInput(attrs={
            'class':"title"
        })) 

class AmbulanceAddForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = '__all__'

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ('driver_name','district')