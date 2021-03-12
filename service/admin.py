from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderedService)
admin.site.register(ServiceDeliveryAddress)
