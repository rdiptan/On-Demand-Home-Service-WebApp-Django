from django import forms
  
# creating a form 
class AvailabilityForm(forms.Form):
    available = forms.BooleanField()