from django.forms import ModelForm
from django.forms import widgets
from django.forms.fields import DateField, DateTimeField, TimeField
from django.forms.widgets import DateInput, PasswordInput
from .models import booking
from django import forms
from django.contrib.auth.forms import AuthenticationForm






class dateinput(forms.DateInput):
    input_type = "date"
class timeinput(forms.TimeInput):
    input_type = "time"

class booking_form(ModelForm):
    
    
    
    class Meta:
        model = booking
        fields = ['source','destination','date','time','vehicle_type']
        
        widgets = {
            'date':dateinput(),
            'time':timeinput(),
            'source': forms.TextInput(attrs={'placeholder': 'Type Source'}),
            'destination': forms.TextInput(attrs={'placeholder': 'Type Destination'}),
            
            
        }
#widgets = {
 #           'name': forms.TextInput(attrs={'placeholder': 'Name'}),
  #          'description': forms.Textarea(
   #             attrs={'placeholder': 'Enter description here'}),
    #    }

class booking_confirm_form(ModelForm):
    
    
    
    class Meta:
        model = booking
        fields = ['source','destination','date','time','vehicle_type','driver_details','booking_status']
        
        





       
