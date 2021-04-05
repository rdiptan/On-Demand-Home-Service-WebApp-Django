from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.views.generic import View, ListView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.auth import admin_only

from accounts.models import Customer

# Create your views here.

@login_required(login_url='login')
def order_view(request, id):
    customer = Customer.objects.get(id=id)
    order_view = Order.objects.all()
    context = {
        'customer' : customer,
        'orderitems': order_view
    }
    return render(request, 'order/orderView.html', context)


@login_required(login_url='login')
def order(request):
    if request.user.is_customer:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderedservice_set.all()
    else:
        items = []
    context = {
        'items': items
    }
    return render(request, 'order/order.html', context)

@login_required(login_url='login')
# def checkout(request, customer, service, description, address, street):
    # order = Order.objects.create()
def checkout(request):
    # service = Service.objects.get(id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(checkout)
    context = {
        'form': OrderForm
    }
    return render(request, 'order/orderform.html', context)


# @login_required
@method_decorator(admin_only , name='dispatch')
class ServicemenOrderDetailView(DetailView):
    template_name = "order/servicemenorderdetail.html"
    model = Order
    context_object_name = "ord_obj"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = Order.STATUS
        return context
 
# @login_required
@method_decorator(admin_only , name='dispatch')
class ServicemenOrderListView(ListView):
    template_name = "order/servicemenorderlist.html"
    queryset = Order.objects.all().order_by("-id")
    context_object_name = "allorders"
 
# @login_required
@method_decorator(admin_only , name='dispatch') 
class ServicemenOrderStatuChangeView(View):
    def post(self, request,*args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
 
        new_status = request.POST.get("status")
        print(new_status)
        order_obj.status = new_status
        order_obj.save()
        return redirect(reverse_lazy("servicemen_order_detail", kwargs={"pk": order_id}))
