from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def service(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'service/service.html', context)


def order(request):
    context = {
        
    }
    return render(request, 'service/order.html', context)


def checkout(request):
    context = {

    }
    return render(request, 'service/checkout.html', context)
