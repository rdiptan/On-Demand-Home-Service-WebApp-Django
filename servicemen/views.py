from django.shortcuts import redirect, render
from order.models import Order
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView
from django.utils.decorators import method_decorator
from accounts.auth import admin_only
from accounts.models import *
from .forms import *
from django.http import HttpResponse


# Create your views here.

# @login_required
# @method_decorator(admin_only , name='dispatch')
class ServicemenOrderDetailView(DetailView):
    template_name = "servicemen/servicemenorderdetail.html"
    model = Order
    context_object_name = "ord_obj"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = Order.STATUS
        return context
 
# @login_required
# @method_decorator(admin_only , name='dispatch')
class ServicemenOrderListView(ListView):
    template_name = "servicemen/servicemenorderlist.html"
    queryset = Order.objects.all().order_by("-id")
    context_object_name = "allorders"
 
# @login_required
# @method_decorator(admin_only , name='dispatch') 
class ServicemenOrderStatuChangeView(View):
    def post(self, request,*args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
 
        new_status = request.POST.get("status")
        print(new_status)
        order_obj.status = new_status
        order_obj.save()
        if new_status == "Expert Assigned":
            ser_id = ServiceMen.objects.filter(created_by = request.user).first()
            order_obj.servicemen = ser_id
            order_obj.save()
        return redirect(reverse_lazy("servicemen_order_detail", kwargs={"pk": order_id}))

def availability(request):
    context ={

    }
    servicemen = ServiceMen.objects.filter(created_by = request.user).first()
    context['servicemen'] = servicemen
    if request.method == 'POST':
        if "change_availability" in request.POST:
            servicemen.is_available = not servicemen.is_available
            servicemen.save()
    return render(request, "servicemen/serviceDashboard.html", context)


# def availability(request):
#     # servicemen = ServiceMen.objects.filter(created_by = request.user).first()
#     # print(servicemen.availabity)
#     # context = {
#     #     'servicemen' : servicemen,
#     # }
#     # return render(request, 'servicemen/serviceDashboard.html', context)
#     context = {}
#     context['form'] = AvailabilityForm()
#     if request.GET:
#         temp = request.GET['available']
#         print(temp)
#     return render( request, "servicemen/serviceDashboard.html", context)

# def home(request):
#     servicemenid = ServiceMen.objects.filter(created_by = request.user).first()
#     w, created = ServiceMen.objects.get_or_create(id=1)
#     return render(request,'servicemen/home.html', {'servicemen': w})

# def toggle(request):
#     w = ServiceMen.objects.get(id=request.POST['id'])
#     w.is_available = request.POST['isavailable'] == 'true'
#     w.save()
#     return HttpResponse('success')
