from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        exclude = ('customer', 'service', 'status')
        model = Order
        

    def save(self, customer, service):
        print(service)
        orderform = Order.objects.create(customer=customer, service=service, description=self.cleaned_data['description'], address=self.cleaned_data['address'],street=self.cleaned_data['street'])
        return orderform