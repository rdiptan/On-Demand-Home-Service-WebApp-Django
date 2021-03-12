from django.urls import path
from . import views

urlpatterns = [
    path('', views.service, name="service"),
    path('order/', views.order, name="order"),
    path('checkout/', views.checkout, name="checkout"),
]