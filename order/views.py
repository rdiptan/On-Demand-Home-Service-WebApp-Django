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
