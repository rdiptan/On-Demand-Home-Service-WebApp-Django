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

def add_service(request):
    form = ServiceForm()
    context = {
        'form': form
    }
    return render(request, 'service/addService.html', context)


def post_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getservice')
    context = {
        'form': ServiceForm
    }
    return render(request, 'service/postService.html', context)

def get_service(request):
    service = Service.objects.all()
    context = {
        'service': service
    }
    return render(request, 'service/getService.html', context)

def update_service(request, service_id):
    instance = Service.objects.get(id= service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('getservice')
    context = {
        'form': ServiceForm(instance=instance)
    }
    return render(request, 'service/updateService.html', context)

def delete_service(request, service_id):
    service = Service.objects.get(id = service_id)
    service.delete()
    return redirect('getservice')