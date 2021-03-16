from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def service(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'service/service.html', context)

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
    return render(request, 'service/order.html', context)

@login_required(login_url='login')
def checkout(request):
    context = {

    }
    return render(request, 'service/checkout.html', context)
