from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_servicemen =  models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

class Customer(models.Model):
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.OneToOneField(User, related_name='customeruser', on_delete=models.CASCADE)

    def __str__(self):
        # return self.first_name + ' ' + self.last_name
        return str(self.id)


class ServiceMen(models.Model):  
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)
    expertise = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='servicmenuser', on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ['created_by']

    def __str__(self):
        # return self.first_name + ' ' + self.last_name
        return str(self.created_by)