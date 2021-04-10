from django.shortcuts import render, redirect
from .models import *
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, get_object_or_404
import random

# Create your views here.

def service(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'service/service.html', context)

def view_service(request, service_slug):
    services = get_object_or_404(Service, slug=service_slug)

    return render(request, 'service/service_view.html', {'services': services})   
