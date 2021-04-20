from django.shortcuts import render, redirect
from service.models import *
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order
from .forms import ProductForm
from django.views.generic import ListView, CreateView, DetailView, View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from .filters import Order
from service.forms import ServiceForm
from admins.filters import OrderFilter
User = get_user_model()

# Create your views here.
@login_required
@admin_only
def admin_dashboard(request):
    service = Service.objects.all()
    service_count = service.count()
    order = Order.objects.all()
    order_count = order.count()
    new_order = Order.objects.filter(status = 'Pending')
    new_order_count = new_order.count()
    users = User.objects.all()
    admin_count = users.filter(is_staff=1).count()
    customer_count = users.filter(is_customer=1).count()
    servicemen_count = users.filter(is_servicemen=1).count()

    context = {
        'service': service_count,
        'order': order_count,
        'new_order': new_order_count,
        'admin': admin_count,
        'customer': customer_count,
        'servicemen': servicemen_count,
        'activate_admin' : 'active'
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
        'form': UserCreationForm,
        'activate_changeadmin' : 'active'

    }
    return render(request, 'admins/register-user-admin.html', context)


@login_required
@admin_only
def get_user(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users': users,
        'activate_admin_user' : 'active'

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

    def get_context_data(self, **kwargs):
        context = super(AdminServiceListView, self).get_context_data(**kwargs)
        context['admin_service'] = 'active'
        return context

 
@method_decorator(admin_only , name='dispatch')
class AdminServiceCreateView(CreateView):
    template_name = "admins/adminservicecreate.html"
    form_class = ProductForm
    success_url = reverse_lazy("view_service")
 
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AdminServiceCreateView, self).get_context_data(**kwargs)
        context['admin_services_create'] = 'active'
        return context

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
        'form': ServiceForm(instance=instance),
        'activate_update_service' : 'active'

    }
    return render(request, 'admins/updateService.html', context)

@login_required
@admin_only
def delete_service(request, service_id):
    service = Service.objects.get(id = service_id)
    service.delete()
    return redirect('view_service')

@method_decorator(admin_only , name='dispatch')
class ServicemenOrderDetailView(DetailView):
    template_name = "admins/servicemenorderdetail.html"
    model = Order
    context_object_name = "ord_obj"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = Order.STATUS
        context['admin_order_detail1'] = 'active'
        return context
 
@login_required
@admin_only
def ServicemenOrderListView(request):
    allorders = Order.objects.all().order_by("-id")
    order_filter = OrderFilter(request.GET, queryset=allorders)
    order_final = order_filter.qs
    context = {
        'allorders': order_final,
        'order_filter': order_filter,
        'activate_all_order' : 'active'
    }
    return render(request, "admins/servicemenorderlist.html", context)
 
@method_decorator(admin_only , name='dispatch') 
class ServicemenOrderStatuChangeView(View):
    def post(self, request,*args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
        new_status = request.POST.get("status")
        print(new_status)
        order_obj.status = new_status
        order_obj.save()
        return redirect(reverse_lazy("admin_servicemen_order_detail", kwargs={"pk": order_id}))
    
    def get_context_data(self, **kwargs):
        context = super(ServicemenOrderStatuChangeView, self).get_context_data(**kwargs)
        context['admin_order_status'] = 'active'
        return context

# @method_decorator(admin_only , name='dispatch')
# class ServicemenNewOrderListView(ListView):
#     template_name = "admins/servicemenorderlist.html"
#     queryset = Order.objects.filter(status = 'Pending').order_by("-id")
#     context_object_name = "allorders"

#     def get_context_data(self, **kwargs):
#         context = super(ServicemenNewOrderListView, self).get_context_data(**kwargs)
#         context['admin_new_order'] = 'active'
#         return context

@login_required
@admin_only
def ServicemenNewOrderListView(request):
    allorders = Order.objects.filter(status = 'Pending').order_by("-id")
    order_filter = OrderFilter(request.GET, queryset=allorders)
    order_final = order_filter.qs
    context = {
        'allorders': order_final,
        'order_filter': order_filter,
        'admin_new_order' : 'active'
    }
    return render(request, "admins/servicemenorderlist.html", context)

@method_decorator(admin_only , name='dispatch')
class ServicemenView(ListView):
    template_name = "admins/servicemenlist.html"
    queryset = ServiceMen.objects.all()
    context_object_name = "allservicemen"

    def get_context_data(self, **kwargs):
        context = super(ServicemenView, self).get_context_data(**kwargs)
        context['admin_view_servicemen'] = 'active'
        return context
