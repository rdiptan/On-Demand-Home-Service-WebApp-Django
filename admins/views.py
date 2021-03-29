from django.shortcuts import render, redirect
from service.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
@login_required
@admin_only
def admin_dashboard(request):
    service = Service.objects.all()
    service_count = service.count()
    order = Order.objects.all()
    order_count = order.count()
    users = User.objects.all()
    admin_count = users.filter(is_staff=1).count()
    customer_count = users.filter(is_customer=1).count()
    servicemen_count = users.filter(is_servicemen=1).count()

    context = {
        'service': service_count,
        'order': order_count,
        'admin': admin_count,
        'customer': customer_count,
        'servicemen': servicemen_count,
    }
    return render(request, 'admins/adminDashboard.html', context)


@login_required
@admin_only
def register_user_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Registered Successfully')
            return redirect('/admin-dashboard')
        else:
            messages.add_message(request, messages.ERROR, 'Please provide correct details')
            return render(request, "admins/register-user-admin.html", {'form': form})
    context = {
        'form': UserCreationForm
    }
    return render(request, 'admins/register-user-admin.html', context)


@login_required
@admin_only
def get_user(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users': users,
    }
    return render(request, 'admins/showUser.html', context)


@login_required
@admin_only
def update_user_to_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User has been updated to Admin')
    return redirect('/admin-dashboard')