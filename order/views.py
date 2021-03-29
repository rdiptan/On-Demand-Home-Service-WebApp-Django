from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse

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
    if request.user.is_authenticated:
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
def checkout(request):
    context = {

    }
    return render(request, 'order/checkout.html', context)
