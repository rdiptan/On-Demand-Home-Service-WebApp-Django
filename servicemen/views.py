from django.shortcuts import redirect, render
from order.models import Order
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.auth import admin_only
from accounts.models import *
from .forms import *
from django.http import HttpResponse
from accounts.decorators import *


# Create your views here.

@method_decorator(servicemen_required, name='dispatch')  
class ServicemenOrderDetailView(DetailView):
    template_name = "servicemen/servicemenorderdetail.html"
    model = Order
    context_object_name = "ord_obj"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ser_order_detail'] = 'active'
        context["allstatus"] = Order.STATUS
        return context
 
@login_required
@servicemen_required
def ServicemenOrderListView(request):
    ser_id = ServiceMen.objects.filter(created_by = request.user).first()
    allorders = Order.objects.filter(servicemen = ser_id).order_by("-id")
    context = {
        'allorders': allorders,
        'ser_order_list': 'active'
    }
    return render(request, "servicemen/servicemenorderlist.html", context)
 
@method_decorator(servicemen_required, name='dispatch') 
class ServicemenOrderStatuChangeView(View):

    def get_context_data(self, **kwargs):
        context = super(ServicemenOrderStatuChangeView, self).get_context_data(**kwargs)
        context['ser_order_status'] = 'active'
        return context

    def post(self, request,*args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
 
        new_status = request.POST.get("status")
        print(new_status)
        order_obj.status = new_status
        order_obj.save()
        if new_status == "Expert Assigned":
            ser_id = ServiceMen.objects.filter(created_by = request.user).first()
            order_obj.servicemen = ser_id
            order_obj.save()
        return redirect(reverse_lazy("servicemen_order_detail", kwargs={"pk": order_id}))

@method_decorator(servicemen_required, name='dispatch') 
class ServicemenNewOrderListView(ListView):
    template_name = "servicemen/servicemenorderlist.html"
    queryset = Order.objects.filter(status = 'Pending').order_by("-id")
    context_object_name = "allorders"

    def get_context_data(self, **kwargs):
        context = super(ServicemenNewOrderListView, self).get_context_data(**kwargs)
        context['ser_new_order'] = 'active'
        return context


@login_required
@servicemen_required
def availability(request):
    new_order = Order.objects.filter(status = 'Pending')
    new_order_count = new_order.count()
    ser_id = ServiceMen.objects.filter(created_by = request.user).first()
    serviceman_order = Order.objects.filter(servicemen = ser_id)
    your_order_count = serviceman_order.count()
    context ={
        'new_order': new_order_count,
        'your_order': your_order_count,
        'activate_servicemen_admin' : 'active'
    }
    servicemen = ServiceMen.objects.filter(created_by = request.user).first()
    context['servicemen'] = servicemen
    if request.method == 'POST':
        if "change_availability" in request.POST:
            servicemen.is_available = not servicemen.is_available
            servicemen.save()
    return render(request, "servicemen/serviceDashboard.html", context)
