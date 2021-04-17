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
def order_view(request):
    customer = customer = Customer.objects.filter(created_by = request.user).first()
    order_view = Order.objects.filter(customer_id=customer.id)
    context = {
        'customer' : customer,
        'orderitems': order_view
    }
    return render(request, 'order/orderView.html', context)

@login_required(login_url='login')
def checkout(request, id):
    customer = Customer.objects.filter(created_by = request.user).first()
    # service_id = request.GET.get('service_id')
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(customer, service)
            return redirect('thankyou')
    context = {
        'form': OrderForm
    }
    return render(request, 'order/orderform.html', context)

def thankyou(request):
    return render(request, 'order/thankyou.html')