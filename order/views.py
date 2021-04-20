from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.views.generic import View, ListView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from accounts.auth import admin_only
from accounts.decorators import *
from accounts.models import Customer

# Create your views here.

@login_required
@customer_required
def order_view(request):
    customer = customer = Customer.objects.filter(created_by = request.user).first()
    order_view = Order.objects.filter(customer_id=customer.id)
    context = {
        'customer' : customer,
        'orderitems': order_view,
        'activate_order' : 'active'
    }
    return render(request, 'order/orderView.html', context)

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

@login_required
@customer_required
def checkout(request, id):
    customer = Customer.objects.filter(created_by = request.user).first()
    # service_id = request.GET.get('service_id')
    service = Service.objects.get(id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(customer, service)
            template = render_to_string('order/mailbody.html', {'name':request.user.first_name, 'service':service.name})

            email = EmailMessage(
                'Thank you for ordering our service',
                template,
                settings.EMAIL_HOST_USER,
                [request.user.email],
            )
            email.fail_silently = False
            email.send()
            return redirect('thankyou')
    context = {
        'service': service,
        'form': OrderForm,
        'order_checkout' : 'active'
    }
    return render(request, 'order/orderform.html', context)

@login_required
@customer_required
def thankyou(request):
    context = {
        'activate_thanks' : 'active'
    }
    return render(request, 'order/thankyou.html', context)
