from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .models import User, Customer, ServiceMen
from .forms import CustomerSignUpForm, ServicemenSignUpForm, CustomerProfileForm, ServicemenProfileForm, UserForm
from django.urls import reverse_lazy
from .auth import unauthenticated_user
from django.core.mail import message
from django.contrib.auth.decorators import login_required
from .decorators import *

# Create your views here.

@unauthenticated_user
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('service')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_customer:
                    login(request, user)
                    return redirect('service')
                elif user.is_servicemen:
                    login(request, user)
                    return redirect('service')
                elif user.is_staff:
                    login(request, user)
                    return redirect('admin_dashboard')
            else:
                messages.add_message(request, messages.INFO, 'Username or Password is incorrect')

        context = {
            'activate_login' : 'active'
        }
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# @unauthenticated_user
class registerCustomer(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "accounts/registercustomer.html"

    def get_context_data(self, **kwargs):
        context = super(registerCustomer, self).get_context_data(**kwargs)
        context['cus_reg'] = 'active'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('service')

# @unauthenticated_user
class registerServicemen(CreateView):
    model = User
    form_class = ServicemenSignUpForm
    template_name = "accounts/registerservicemen.html"

    def get_context_data(self, **kwargs):
        context = super(registerServicemen, self).get_context_data(**kwargs)
        context['ser_reg'] = 'active'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('service')

@login_required
@customer_required
def customerAccount(request):
    profile = request.user
    cus_id = Customer.objects.filter(created_by = request.user).first()
    if request.method == 'POST':
        user_u = UserForm(request.POST, instance=profile)
        profile_u = CustomerProfileForm(request.POST, instance=cus_id)
        if user_u.is_valid() and profile_u.is_valid:
            user_u.save()
            profile_u.save()
            messages.success(request, 'Account Update Sucessful for' + str(request.user))
            return redirect('customer_profile')
    else:
        user_u = UserForm(instance=profile)
        profile_u = CustomerProfileForm(instance=cus_id)
    context = {
        'form1': user_u,
        'form2': profile_u,
        'cus_id': cus_id,
        'activate_cusacc' : 'active'
        }
    return render(request, 'accounts/profile.html', context)

@login_required
@servicemen_required
def servicemenAccount(request):
    profile = request.user
    ser_id = ServiceMen.objects.filter(created_by = request.user).first()
    if request.method == 'POST':
        user_u = UserForm(request.POST, instance=profile)
        profile_u = ServicemenProfileForm(request.POST, instance=ser_id)
        if user_u.is_valid() and profile_u.is_valid:
            user_u.save()
            profile_u.save()
            messages.success(request, 'Account Update Sucessful for ' + str(request.user))
            return redirect('servicemen_profile')
    else:
        user_u = UserForm(instance=profile)
        profile_u = ServicemenProfileForm(instance=ser_id)
    context = {
        'form1': user_u,
        'form2': profile_u,
        'ser_id': ser_id,
        'activate_seracc' : 'active'
        }
    return render(request, 'accounts/profile.html', context)
