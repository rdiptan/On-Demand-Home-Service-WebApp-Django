from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .models import User
from .forms import CustomerSignUpForm, ServicemenSignUpForm, CustomerProfileForm, ServicemenProfileForm
from django.urls import reverse_lazy
from .auth import unauthenticated_user
from django.core.mail import message

# Create your views here.

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

        }
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

class registerCustomer(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "accounts/registercustomer.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('service')

class registerServicemen(CreateView):
    model = User
    form_class = ServicemenSignUpForm
    template_name = "accounts/registerservicemen.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('service')

def customerAccount(request):
    profile = request.user.customeruser
    form = CustomerProfileForm(instance = profile)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            message.success(request, 'Account Update Sucessful for' + str(request.user.customeruser))
            return redirect('customer_account')
    context = {'form': form}
    return render(request, 'accounts/profile.html', context)

def servicemenAccount(request):
    profile = request.user.servicemenuser
    form = ServicemenProfileForm(instance = profile)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            message.success(request, 'Account Update Sucessful for' + str(request.user.servicemenuser))
            return redirect('customer_account')
    context = {'form': form}
    return render(request, 'accounts/profile.html', context)