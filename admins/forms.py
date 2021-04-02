from service.models import Service
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "description", "image",]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
            "description": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the service description here..."
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),     
        }