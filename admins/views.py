from django.shortcuts import render, redirect
from service.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order
from .forms import ProductForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from service.forms import ServiceForm
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

@method_decorator(admin_only , name='dispatch')
class AdminServiceListView(ListView):
    template_name = "admins/getService.html"
    queryset = Service.objects.all().order_by("-id")
    context_object_name = "service"

 
@method_decorator(admin_only , name='dispatch')
class AdminServiceCreateView(CreateView):
    template_name = "admins/adminservicecreate.html"
    form_class = ProductForm
    success_url = reverse_lazy("view_service")
 
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required
@admin_only
def update_service(request, service_id):
    instance = Service.objects.get(id= service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('getservice')
    context = {
        'form': ServiceForm(instance=instance)
    }
    return render(request, 'admins/updateService.html', context)

@login_required
@admin_only
def delete_service(request, service_id):
    service = Service.objects.get(id = service_id)
    service.delete()
    return redirect('view_service')
