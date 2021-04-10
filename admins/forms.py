from service.models import Service
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "slug", "description", "image",]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
            "slug": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the service slug here..."
            }),
            "description": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the service description here..."
            }),
            "image": forms.ClearableFileInput(attrs={
            }),     
        }