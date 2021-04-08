from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name="order"),
    path('orderview/<int:id>/', views.order_view, name="orderview"),
    path('checkout/<int:id>/', views.checkout, name="checkout"),

]