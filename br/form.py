from django import forms
from django.forms import fields
from .models import BloodRequest
from django.contrib.admin import widgets 
from django.forms.widgets import DateTimeInput, Widget, Select, MultiWidget                                      
from django.contrib.admin.widgets import AdminDateWidget
from .date_time import MinimalSplitDateTimeMultiWidget





class BloodRequestForm(forms.ModelForm):
    
    incident = forms.CharField(label='Why need Blood', 
                    widget=forms.TextInput(attrs={'placeholder': 'why need blood ? '}))
    contact = forms.CharField(label='phone Number', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))

    
    email = forms.CharField(label='Your personal email', 
                    widget=forms.TextInput(attrs={'placeholder': 'Enter your email id'}))
 
   
    # blood_need_date = forms.DateField(widget=widgets.AdminDateWidget)
    # blood_need_time = forms.TimeField(widget=widgets.AdminTimeWidget)
    # mydatetime = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
   

    blood_need = forms.DateTimeField(widget=MinimalSplitDateTimeMultiWidget())


    class Meta:
        widgets = {
            'content': forms.Textarea(attrs={
               
                'cols': 200, 'rows': 2,
                'placeholder':'Full breif why you need blood?'
                
                }),

                
        }
        model = BloodRequest
        fields = ('incident','blood_group','contact','district','division','email','blood_need','content')
# def __init__(self, *args, **kwargs):
#     super(BloodRequest, self).__init__(*args, **kwargs)
#     mydate = forms.DateField(widget=widgets.AdminDateWidget)
#     mytime = forms.TimeField(widget=widgets.AdminTimeWidget)
#     blood_need = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)

#     self.fields['blood_need'].widget = widgets.AdminSplitDateTime()

def __init__(self, *args, **kwargs):
    super(BloodRequestForm,self).__init__(*args, **kwargs) 
    self.fields['contact'].required=False  


 