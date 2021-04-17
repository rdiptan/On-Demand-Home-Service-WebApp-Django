from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.forms import ModelForm
from django.db import transaction
from .models import *
from django.contrib.auth import password_validation


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(created_by=user)
        customer.phone = self.cleaned_data.get('phone')
        customer.address = self.cleaned_data.get('address')
        customer.save()
        return user

class ServicemenSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=200, required=True)
    expertise = forms.CharField(max_length=200, required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_servicemen = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        servicemen = ServiceMen.objects.create(created_by=user)
        servicemen.phone = self.cleaned_data.get('phone')
        servicemen.address = self.cleaned_data.get('address')
        servicemen.expertise = self.cleaned_data.get('expertise')
        servicemen.save()
        return user

class CustomerProfileForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ServicemenProfileForm(ModelForm):
    class Meta:
        model = ServiceMen
        fields = '__all__'

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
        