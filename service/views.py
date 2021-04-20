from django.shortcuts import render, redirect
from .models import *
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, get_object_or_404
from .filters import serviceFilter

# Create your views here.

def service(request):
    services = Service.objects.all()
    service_filter = serviceFilter(request.GET, queryset=services)
    service_final = service_filter.qs
    context = {
        'services': service_final,
        'service_filter': service_filter,
        'activate_service' : 'active'
    }
    return render(request, 'service/service.html', context)

def view_service(request, service_slug):
    services = get_object_or_404(Service, slug=service_slug)
    context = {
        'services': services,
        'activate_view_service' : 'active'
    }
    return render(request, 'service/service_view.html', context)   

def about(request):
    context = {
        'about' : 'active'
    }
    return render(request, 'service/about.html', context)
