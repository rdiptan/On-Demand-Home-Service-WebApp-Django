from django.shortcuts import redirect, render
from order.models import Order
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView
from django.utils.decorators import method_decorator
from accounts.auth import admin_only

# Create your views here.

# @login_required
@method_decorator(admin_only , name='dispatch')
class ServicemenOrderDetailView(DetailView):
    template_name = "servicemen/servicemenorderdetail.html"
    model = Order
    context_object_name = "ord_obj"
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = Order.STATUS
        return context
 
# @login_required
@method_decorator(admin_only , name='dispatch')
class ServicemenOrderListView(ListView):
    template_name = "servicemen/servicemenorderlist.html"
    queryset = Order.objects.all().order_by("-id")
    context_object_name = "allorders"
 
# @login_required
@method_decorator(admin_only , name='dispatch') 
class ServicemenOrderStatuChangeView(View):
    def post(self, request,*args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
 
        new_status = request.POST.get("status")
        print(new_status)
        order_obj.status = new_status
        order_obj.save()
        return redirect(reverse_lazy("servicemen_order_detail", kwargs={"pk": order_id}))
