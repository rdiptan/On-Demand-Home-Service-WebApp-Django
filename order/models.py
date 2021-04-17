from django.db import models
from accounts.models import Customer, ServiceMen 
from service.models import Service

# Create your models here.

class Order(models.Model):
    STATUS = (
        ("Reviewed", "Reviewed"),
        ("Expert Assigned", "Expert Assigned"),
        ("Working", "Working"),
        ("Finished", "Finished"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=2000, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default="Pending")
    street = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    servicemen = models.ForeignKey(ServiceMen, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['-date_ordered']

    def __str__(self):
        return str(self.id)


class Payment(models.Model):
    OPTION = (
        ("Cash", "Cash"),
        ("Card", "Card"),
        ("FonePay", "FonePay"),
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField(null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    paid_through = models.CharField(max_length=200, null=True, choices=OPTION)
    paid_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)
        